"""supp-cache1: the predeclared per-instance analysis (read-only, offline; written before the launch).

    python3 supp-cache1-analysis.py SUPP_EXPORT CONFIRM1_EXPORT [--json OUT.json] [--markdown OUT.md]

SUPP_EXPORT is the launcher export of supp-cache1 (six guarded sessions with dev-cache1 B's configuration);
CONFIRM1_EXPORT is confirm1's frozen export (its guarded-clm and summary sessions are the reused, non-contemporaneous
baselines). Only exported records are read. Nothing is sent anywhere and no tokenizer is used.

**Per session** (all three arms): score, recall, completed turns, outcome and endings; attempts (main and summariser),
task tool calls, input and output tokens, cache reads, writes and uncached input, confirmed and assumed charges, and
summed model latency. For guarded sessions also accepted and rejected edits, held-back outputs and refetches.

**For the new sessions only, the cache evidence:**
- every attempt is classified as in dev-cache1-analysis.py: first, ordinary, turn_start, after_change or retry;
- **within-turn and new-turn reuse:** an ordinary or turn_start attempt "read the previous marker" when its reported
  read equals the previous attempt's reported read plus written tokens (everything up to that attempt's last
  breakpoint);
- **shared-prefix reuse across sessions:** each session's first attempt's reported read (0 means none was read);
- **the boundary check, now specified prospectively** (the dev-cache1 post-hoc method):
  - *the evidence it combines:* the request each attempt recorded (what the harness built and passed to the adapter,
    from which the working-context entry lines are reconstructed; not the HTTP body) and the provider-reported usage
    (the only token figures);
  - *the rule:* an earlier attempt j's context marker is eligible for attempt k when j's entry lines are a prefix of
    k's and k has at most 19 more entries (the 20-block lookback; the head block counts as position 0). The predicted
    read is the largest such j's read plus written tokens. The 5-minute lifetime is assumed to hold within a session
    (the record checks the session's ledger timestamps, which the export doesn't carry);
  - *when no marker is eligible* (the head is out of reach, more than 19 entries), the prediction is the tools and
    system prompt, whose size is not observed in this layout and may differ per instance. Such attempts are checked
    for consistency only: the read must be positive and smaller than the first request's cached head prefix;
  - *the outcome per session:* exact matches, consistent fallbacks and mismatches (listed).
"""

from __future__ import annotations

import importlib.util
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent


def _load(name: str, file: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


base = _load("dev_cache1_analysis", "dev-cache1-analysis.py")  # sections, user_text, calls (committed, hashed)
read_jsonl = base.read_jsonl
INSTANCES = [f"docthread-confirm-{k}" for k in range(1, 7)]


def find(export: Path, instance: str, arm: str) -> Path | None:
    hits = [p.parent for p in export.rglob("session.json") if p.parent.name.endswith(f"-{instance}-{arm}.r1")]
    return hits[0] if len(hits) == 1 else None


def session_figures(run: Path) -> dict[str, Any]:
    session = json.loads((run / "session.json").read_text(encoding="utf-8"))
    rows = read_jsonl(run / "attempts.jsonl")
    finished = [r for r in rows if r["event"] == "finished"]
    rep = [r.get("reported") or {} for r in finished]
    result = session.get("launch_result") or {}
    trace = read_jsonl(run / "trace.jsonl")
    count = lambda t: sum(1 for r in trace if r.get("type") == t)  # noqa: E731
    out = {
        "run_id": session["run_id"],
        "points": result.get("points"), "out_of": result.get("out_of"), "recall_points": result.get("recall_points"),
        "completed_turns": sum(1 for e in result.get("endings") or [] if e == "completed"),
        "outcome": result.get("outcome"), "endings": result.get("endings"),
        "attempts": len(finished),
        "attempts_by_category": result.get("attempts_by_category"),
        "task_tool_calls": sum(len(t) for t in session.get("calls_by_turn") or []),
        "input_tokens": sum(r.get("input_tokens_total") or 0 for r in rep),
        "output_tokens": sum(r.get("output_tokens") or 0 for r in rep),
        "cache_read": sum(r.get("cache_read_tokens") or 0 for r in rep),
        "cache_written": sum(r.get("cache_write_tokens") or 0 for r in rep),
        "uncached": sum(r.get("input_tokens_uncached") or 0 for r in rep),
        "confirmed_usd": round(sum(r.get("charged_usd", 0.0) for r in finished if r.get("cost_basis") == "provider_usage"), 6),
        "assumed_usd": round(sum(r.get("charged_usd", 0.0) for r in finished if r.get("cost_basis") not in (None, "provider_usage")), 6),
        "latency_s": round(sum(r.get("latency_s") or 0.0 for r in finished), 1),
    }  # fmt: skip
    if "guarded_clm" in (session.get("provenance") or {}) and "arm" not in session:
        edits = [r.get("status") for r in trace if r.get("type") == "lite_edit"]
        out |= {"edits_accepted": edits.count("accepted"), "edits_rejected": edits.count("rejected"),
                "held_back": count("lite_held_back"), "refetches": count("lite_refetch")}  # fmt: skip
    return out


def cache_evidence(run: Path) -> dict[str, Any]:
    calls = base.calls(run)
    started = {r["attempt"]: r for r in read_jsonl(run / "attempts.jsonl") if r["event"] == "started"}
    entries = {k: base.sections(base.user_text(s))[1] for k, s in started.items()}
    out: dict[str, Any] = {"first_attempt_read": calls[0]["cache_read_tokens"] if calls else None}
    by_class: dict[str, dict[str, Any]] = {}
    for c in ("ordinary", "turn_start", "after_change", "retry"):
        rs = [i for i, r in enumerate(calls) if r["class"] == c]
        prev_marker = sum(1 for i in rs if i and calls[i]["cache_read_tokens"] ==
                          calls[i - 1]["cache_read_tokens"] + calls[i - 1]["cache_write_tokens"])  # fmt: skip
        tot = sum(calls[i]["input_tokens_total"] or 0 for i in rs)
        read = sum(calls[i]["cache_read_tokens"] or 0 for i in rs)
        by_class[c] = {"attempts": len(rs), "read_previous_marker": prev_marker,
                       "read_share": round(read / tot, 4) if tot else None, "exercised": bool(rs)}  # fmt: skip
    out["by_class"] = by_class
    head = (calls[0]["cache_read_tokens"] + calls[0]["cache_write_tokens"]) if calls else 0
    exact, consistent, mismatches = 0, 0, []
    for i, c in enumerate(calls):
        if i == 0:
            continue
        e = entries[c["attempt"]]
        best = None
        for j in calls[:i]:
            ej = entries[j["attempt"]]
            if e[: len(ej)] == ej and len(e) - len(ej) <= 19:
                cached = j["cache_read_tokens"] + j["cache_write_tokens"]
                best = cached if best is None else max(best, cached)
        got = c["cache_read_tokens"]
        if best is not None and got == best:
            exact += 1
        elif best is None and 0 < got < head:
            consistent += 1
        else:
            mismatches.append({"attempt": c["attempt"], "class": c["class"], "observed": got, "predicted": best})
    out["boundary_check"] = {"attempts_checked": max(0, len(calls) - 1), "exact": exact,
                             "consistent_tools_and_system_fallback": consistent, "mismatches": mismatches}  # fmt: skip
    return out


def collect(supp: Path, confirm1: Path) -> dict[str, Any]:
    out: dict[str, Any] = {"instances": {}}
    for inst in INSTANCES:
        row: dict[str, Any] = {}
        new = find(supp, inst, "guarded_clm")
        row["new_guarded"] = (session_figures(new) | {"cache": cache_evidence(new)}) if new else None
        for key, arm in (("confirm1_guarded", "guarded_clm"), ("confirm1_summary", "token_tail_p015")):
            run = find(confirm1, inst, arm)
            row[key] = session_figures(run) if run else None
        out["instances"][inst] = row
    totals: dict[str, Any] = {}
    for key in ("new_guarded", "confirm1_guarded", "confirm1_summary"):
        rows = [r[key] for r in out["instances"].values() if r[key]]
        totals[key] = {f: round(sum(r[f] or 0 for r in rows), 6) for f in
                       ("points", "out_of", "recall_points", "completed_turns", "attempts", "task_tool_calls",
                        "input_tokens", "output_tokens", "cache_read", "cache_written", "uncached", "confirmed_usd",
                        "assumed_usd", "latency_s")} | {"sessions": len(rows)}  # fmt: skip
    out["totals"] = totals
    out["generated_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
    return out


def markdown(d: dict[str, Any]) -> str:
    cols = ("points", "recall_points", "completed_turns", "outcome", "confirmed_usd", "latency_s", "attempts",
            "task_tool_calls", "input_tokens", "output_tokens", "cache_read", "cache_written", "uncached")  # fmt: skip
    out = ["# supp-cache1: per-instance results (generated by supp-cache1-analysis.py)", ""]
    out += ["| instance | session | " + " | ".join(cols) + " |", "|" + " --- |" * (len(cols) + 2)]
    for inst, row in d["instances"].items():
        for key, label in (("new_guarded", "new guarded (B)"), ("confirm1_guarded", "confirm1 guarded"),
                           ("confirm1_summary", "confirm1 summary")):  # fmt: skip
            r = row[key]
            cells = [str(r[c]) if r else "missing" for c in cols]
            out.append(f"| {inst} | {label} | " + " | ".join(cells) + " |")
    out += ["", "| totals | " + " | ".join(cols) + " |", "|" + " --- |" * (len(cols) + 1)]
    for key, t in d["totals"].items():
        out.append(f"| {key} ({t['sessions']}) | " + " | ".join(str(t.get(c, "")) for c in cols) + " |")
    out += ["", "## Guarded edits, holds and refetches", "", "| instance | session | accepted | rejected | held back | refetches |",
            "| --- | --- | --- | --- | --- | --- |"]  # fmt: skip
    for inst, row in d["instances"].items():
        for key in ("new_guarded", "confirm1_guarded"):
            r = row[key]
            if r:
                out.append(f"| {inst} | {key} | {r['edits_accepted']} | {r['edits_rejected']} | {r['held_back']} | {r['refetches']} |")
    out += ["", "## New sessions: cache evidence", "",
            "| instance | first read | ordinary: prev marker / attempts (share) | turn start: prev marker / attempts (share) | after change: attempts (share) | boundary: exact / fallback / mismatches |",
            "| --- | --- | --- | --- | --- | --- |"]  # fmt: skip
    for inst, row in d["instances"].items():
        r = row["new_guarded"]
        if not r:
            out.append(f"| {inst} | missing | | | | |")
            continue
        c = r["cache"]["by_class"]
        b = r["cache"]["boundary_check"]
        cell = lambda x: f"{x['read_previous_marker']} / {x['attempts']} ({x['read_share']})" if x["exercised"] else "not exercised"  # noqa: E731
        ac = c["after_change"]
        out.append(f"| {inst} | {r['cache']['first_attempt_read']} | {cell(c['ordinary'])} | {cell(c['turn_start'])} | "
                   f"{ac['attempts']} ({ac['read_share']}) | {b['exact']} / {b['consistent_tools_and_system_fallback']} / "
                   f"{len(b['mismatches'])} |")  # fmt: skip
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    d = collect(Path(argv[0]), Path(argv[1]))
    rest = argv[2:]
    if "--json" in rest:
        Path(rest[rest.index("--json") + 1]).write_text(json.dumps(d, indent=1) + "\n")
    text = markdown(d)
    if "--markdown" in rest:
        Path(rest[rest.index("--markdown") + 1]).write_text(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
