"""dev-cache1, post hoc (written after the run, not predeclared): observed cache reads against the eligible boundaries,
the accepted edits, and a cost decomposition. Read-only over the two exports; nothing is sent anywhere.

    python3 dev-cache1-boundary-check.py EXPORT_A EXPORT_B

**The predicted read for a call** is the tokens cached at the furthest eligible earlier breakpoint, under the
documented rules: an exact prefix ending at a block where an earlier request had a breakpoint, within 20 blocks of one
of this request's breakpoints, and within the 5-minute lifetime (every gap here is far shorter).
- **A** (one user block, automatic caching): the user block differs in every request, so the only eligible prefix is
  the tools and system prompt. The predicted read is the size of that prefix, which A's own reads show.
- **B** (one block per entry, a marker on the last entry, the task and status after it): an earlier call j's marker
  is eligible for call k when j's entry lines are a prefix of k's and k has at most 19 more entries. The tokens cached
  there are j's read plus j's written tokens (everything up to j's last breakpoint). If no such j exists, the tools and
  system prefix (A's figure: the two sessions' tools and system prompts differ only in the session tag's hex digits).

Token sizes come only from the provider's reported usage; no tokenizer is used.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("analysis", HERE / "dev-cache1-analysis.py")
analysis = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
spec.loader.exec_module(analysis)  # type: ignore[union-attr]

PRICE = {"input": 2.0, "write": 2.5, "read": 0.2, "output": 10.0}  # USD per million tokens, configs/prices.toml


def entries_by_attempt(run: Path) -> dict[int, list[str]]:
    rows = analysis.read_jsonl(run / "attempts.jsonl")
    return {r["attempt"]: analysis.sections(analysis.user_text(r))[1] for r in rows if r["event"] == "started"}


def predicted_b(calls: list[dict], entries: dict[int, list[str]], tools_system: int) -> list[tuple[int, int, str]]:
    out = []
    for i, c in enumerate(calls):
        e = entries[c["attempt"]]
        best, source = tools_system, "tools and system"
        for j in calls[:i]:
            ej = entries[j["attempt"]]
            if e[: len(ej)] == ej and len(e) - len(ej) <= 19:
                cached = j["cache_read_tokens"] + j["cache_write_tokens"]
                if cached > best:
                    best, source = cached, f"attempt {j['attempt']}'s marker ({len(ej)} entries)"
        out.append((c["attempt"], best if i else 0, source if i else "none (first request)"))
    return out


def cost(calls: list[dict]) -> dict[str, float]:
    parts = {
        "written": sum(c["cache_write_tokens"] for c in calls) * PRICE["write"] / 1e6,
        "read": sum(c["cache_read_tokens"] for c in calls) * PRICE["read"] / 1e6,
        "uncached": sum(c["input_tokens_uncached"] for c in calls) * PRICE["input"] / 1e6,
        "output": sum(c["output_tokens"] for c in calls) * PRICE["output"] / 1e6,
    }
    return {k: round(v, 6) for k, v in parts.items()} | {"total": round(sum(parts.values()), 6)}


def main(argv: list[str]) -> int:
    runs = [analysis.session_dir(Path(x)) for x in argv[:2]]
    a_calls, b_calls = (analysis.calls(r) for r in runs)
    tools_system = a_calls[1]["cache_read_tokens"]
    print(f"tools and system prefix (A's reads): {sorted({c['cache_read_tokens'] for c in a_calls[1:]})}")
    print("\n## A: observed read against the predicted tools-and-system prefix")
    print("mismatches:", [(c["attempt"], c["cache_read_tokens"]) for c in a_calls[1:] if c["cache_read_tokens"] != tools_system])
    print("\n## B: observed against predicted (attempt, class, observed, predicted, source)")
    entries = entries_by_attempt(runs[1])
    matches = 0
    for (k, pred, src), c in zip(predicted_b(b_calls, entries, tools_system), b_calls, strict=True):
        ok = c["cache_read_tokens"] == pred
        matches += ok
        print(f"{k:3d} {c['class']:12s} {c['cache_read_tokens']:6d} {pred:6d} {'=' if ok else '!='} {src}")
    print(f"B: {matches} of {len(b_calls)} attempts read exactly the predicted prefix")

    print("\n## Accepted edits (trace) and B's next request")
    for name, run in zip("AB", runs, strict=True):
        trace = analysis.read_jsonl(run / "trace.jsonl")
        for r in trace:
            if r.get("type") == "lite_edit":
                ops = json.loads(r.get("code") or "[]")
                print(f"{name} step {r.get('step')}: {r.get('status')}; ops {[(o.get('op'), o.get('ids') or o.get('id')) for o in ops]}")

    print("\n## Volume and cost")
    for name, calls in (("A", a_calls), ("B", b_calls)):
        tin = sum(c["input_tokens_total"] for c in calls)
        out = sum(c["output_tokens"] for c in calls)
        print(f"{name}: attempts {len(calls)}, input {tin}, output {out}, cost by component {cost(calls)}")
    # B's own requests priced as A's configuration bills them: the tools and system prefix read, the rest written.
    as_a = sum(tools_system * PRICE["read"] + (c["input_tokens_total"] - tools_system) * PRICE["write"]
               for c in b_calls[1:]) / 1e6 + b_calls[0]["input_tokens_total"] * PRICE["write"] / 1e6
    b = cost(b_calls)
    print(f"B's input as billed: {round(b['written'] + b['read'] + b['uncached'], 6)}; "
          f"the same input billed as A bills (an estimate): {round(as_a, 6)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
