"""012 offline opportunity audit: how large are the tool results a CLM agent actually receives?

Usage (from this folder):  python audit_observations.py  [writes audit_output.json, prints tables]

Fixed trace set (see ../protocol.md): every observation of the 12 condition-A (ordinary CLM)
runs of experiment 010 v3's exported evaluation. Reads only exported artifacts; no API calls.

Measured per execution step, keeping the stages apart:
  1. source:   size of the fixture files released so far (what *could* be read);
  2. produced: bytes the command wrote to stdout/stderr (executor count, before the cap);
  3. retained: characters kept after the 6,000-character-per-stream cap (the observation body);
  4. received: whether that observation was in the next model request, and in how many later
               requests it stayed before an edit removed it or the runtime spilled it;
  5. later:    context edits that removed it, spills, and later rereads of the same file.
Exact token counts exist only per request (provider usage); the share of a request taken by
observations is estimated from character shares and labelled as an estimate. The cost estimate
follows prompt caching: an observation is written to the cache once (cache-write price) and
then read from it (cache-read price) for each later request that still contains it.

Scorer truth (evidence lines) is used only to check, afterwards, whether known evidence lines
appeared in the observations. It is not, and must not become, an input to any filter.
"""

from __future__ import annotations

import json
import re
import statistics as st
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE.parents[1] / "010-jev-initiated-review" / "artifacts"
RUNS = sorted(
    p for p in (ART / "runs" / "v3" / "evaluation").iterdir() if "-clm_helpers-cacheon-rounds-" in p.name
)
PRICE = {"input": 4.00, "cache_write_5m": 5.00, "cache_read": 0.20}  # USD per M, configs/prices.toml
LOG_LINE = re.compile(r"^\s*(?:[\w./-]+\.log[:\s]+)?\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ\s+(INFO|WARN|ERROR|DEBUG)\b")
LEVEL = re.compile(r"\b(INFO|WARN|ERROR|DEBUG)\b")


def parse_user(payload: dict) -> dict:
    text = "".join(b["text"] for b in payload["messages"][0]["content"] if b["type"] == "text")
    sys_text = "".join(b["text"] for b in payload["system"])

    def section(tag: str) -> str:
        m = re.search(rf"<{tag}>\n?(.*?)\n?</{tag}>", text, re.S)
        return m.group(1) if m else ""

    entries = []
    for line in section("working_context").splitlines():
        line = line.strip()
        if line:
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return {
        "system": len(sys_text),
        "task": len(section("task")),
        "status": len(section("runtime_status")),
        "entries": entries,
        "total": len(sys_text) + len(text),
    }


def classify(code: str) -> str:
    """How the model-written command selected its output (heuristic; checked on samples)."""
    reads_fixture = "/task/fixtures" in code or "fixtures" in code
    filt = any(
        k in code
        for k in ("re.search", "re.findall", "re.match", "re.compile", " in l", " in line", "startswith(", "if '", 'if "', "Counter(", ".count(", "[:")
    )
    dump = bool(re.search(r"print\(\s*open\([^)]*\)\.read\(\)\s*\)", code)) or "print(f.read())" in code
    if not reads_fixture:
        return "no fixture read (workspace, context or helpers)"
    if dump and not filt:
        return "whole-file print"
    if dump and filt:
        return "whole-file print + filtered extraction"
    if filt:
        return "filtered extraction"
    return "fixture read, other"


def evidence_lines(truth: dict, fixtures: Path) -> set[str]:
    out = set()
    for inc in truth.get("incidents", []):
        for refs in inc.get("evidence_groups", {}).values():
            for path, line in refs:
                f = fixtures / path
                if f.is_file():
                    lines = f.read_text().splitlines()
                    if 0 < line <= len(lines):
                        out.add(lines[line - 1].strip())
    return out


def audit_run(run: Path) -> dict:
    meta = json.loads((run / "run.json").read_text())
    task = meta["task"]
    fx = ART / "fixtures" / task
    ev = [json.loads(x) for x in (run / "events.jsonl").read_text().splitlines()]
    truth = json.loads((run / "evaluator" / "truth.json").read_text())
    ev_lines = evidence_lines(truth, fx)
    stage, stage_at = 1, {}
    for e in ev:
        if e["event"] == "stage_released":
            stage = e["stage"]
        if "step" in e:
            stage_at.setdefault(e["step"], stage)
    # requests in order, with their step and exact usage
    reqs = []
    usage = {e["step"]: e["usage"] for e in ev if e["event"] == "response" and e["kind"] == "action"}
    for p in sorted((run / "requests").glob("*.json")):
        d = json.loads(p.read_text())
        if d["meta"]["kind"] != "action":
            continue
        u = parse_user(d["payload"])
        u["step"] = d["meta"]["step"]
        u["usage"] = usage.get(u["step"], {})
        reqs.append(u)
    spills = {e["entry"]: e for e in ev if e["event"] == "spill"}
    obs = []
    for e in ev:
        if e["event"] != "execution_result":
            continue
        step = e["step"]
        code = (run / "scripts" / f"step-{step:03d}.py").read_text()
        oid = f"s{step}.obs"
        later = [r for r in reqs if r["step"] > step]
        bodies = [next((x["body"] for x in r["entries"] if x["id"] == oid), None) for r in later]
        first = bodies[0] if bodies else None
        resident = 0
        for b in bodies:
            if b is None or b.startswith("[runtime: observation of"):
                break
            resident += 1
        stdout = e["stdout"] or ""
        levels = Counter(m.group(1) for line in stdout.splitlines() if (m := LEVEL.search(line)))
        loglines = [line for line in stdout.splitlines() if LOG_LINE.search(line) or LEVEL.search(line)]
        released = sum(
            f.stat().st_size
            for f in fx.rglob("*")
            if f.is_file() and f.name != "SHA256SUMS" and int(f.relative_to(fx).parts[0][6:8]) <= stage_at.get(step, 1)
        )
        obs.append(
            {
                "step": step,
                "stage": stage_at.get(step, 1),
                "released_fixture_bytes": released,
                "produced_bytes": e["stdout_bytes"] + e["stderr_bytes"],
                "retained_chars": len(stdout) + len(e["stderr"] or ""),
                "truncated": e["stdout_bytes"] > len(stdout.encode()) or e["stderr_bytes"] > len((e["stderr"] or "").encode()),
                "observation_chars": len(first) if first is not None else None,
                "in_next_request": first is not None and not first.startswith("[runtime:"),
                "requests_resident": resident,
                "spilled": oid in spills,
                "command": classify(code),
                "log_lines": len(loglines),
                "levels": dict(levels),
                "evidence_lines_present": sum(1 for x in ev_lines if x and x in stdout),
                "stdout_lines": len(stdout.splitlines()),
            }
        )
    # request composition (characters; tokens exact only as totals)
    comp = []
    for r in reqs:
        by_role = Counter()
        for x in r["entries"]:
            by_role[x["role"]] += len(x["body"])
        u = r["usage"]
        comp.append(
            {
                "step": r["step"],
                "chars_total": r["total"],
                "chars_system": r["system"],
                "chars_task": r["task"],
                "chars_status": r["status"],
                "chars_by_role": dict(by_role),
                "tokens_exact": (u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)),
                "uncached": u.get("input_tokens", 0),
                "cache_read": u.get("cache_read_input_tokens", 0),
                "cache_write": u.get("cache_creation_input_tokens", 0),
            }
        )
    summ = json.loads((run / "summary.json").read_text())
    return {
        "run": run.name,
        "task": task,
        "strict": summ["score"].get("strict_success"),
        "cost_usd": summ["cost"]["incurred_usd"],
        "observations": obs,
        "requests": comp,
        "edits": sum(1 for e in ev if e["event"] == "context_edit" and e.get("changed")),
        "spills": len(spills),
        "fixture_bytes_total": sum(f.stat().st_size for f in fx.rglob("*") if f.is_file() and f.name != "SHA256SUMS"),
    }


def pct(xs: list[float], q: float) -> float:
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(q * (len(xs) - 1))))] if xs else 0


def main() -> None:
    runs = [audit_run(r) for r in RUNS]
    (HERE / "audit_output.json").write_text(json.dumps(runs, indent=1))
    obs = [o for r in runs for o in r["observations"]]
    print(f"runs {len(runs)}; executions {len(obs)}; strict {sum(bool(r['strict']) for r in runs)}/12")
    ret = [o["retained_chars"] for o in obs]
    prod = [o["produced_bytes"] for o in obs]
    print("\nretained observation chars: n %d  median %d  p75 %d  p90 %d  max %d  mean %.0f" % (len(ret), pct(ret, .5), pct(ret, .75), pct(ret, .9), max(ret), st.mean(ret)))
    print("produced bytes:             median %d  p90 %d  max %d" % (pct(prod, .5), pct(prod, .9), max(prod)))
    bins = [(0, 500), (500, 2000), (2000, 4000), (4000, 6000), (6000, 10**9)]
    print("size bins (retained chars):", {f"{a}-{b if b < 10**9 else 'inf'}": sum(a <= x < b for x in ret) for a, b in bins})
    print("truncated by the cap:", sum(o["truncated"] for o in obs), " spilled:", sum(o["spilled"] for o in obs))
    print("in next request:", sum(o["in_next_request"] for o in obs), " mean requests resident: %.1f" % st.mean(o["requests_resident"] for o in obs))
    print("commands:", Counter(o["command"] for o in obs))
    print("released fixture bytes at step: median %d max %d; total fixtures per instance %s" % (pct([o['released_fixture_bytes'] for o in obs], .5), max(o['released_fixture_bytes'] for o in obs), sorted({r['task']: r['fixture_bytes_total'] for r in runs}.items())))
    big = [o for o in obs if o["retained_chars"] >= 2000]
    lv = Counter()
    for o in big:
        lv.update(o["levels"])
    print("observations >= 2000 chars:", len(big), " level counts in them:", dict(lv), " evidence lines present (sum):", sum(o['evidence_lines_present'] for o in big))
    reqs = [q for r in runs for q in r["requests"]]
    tot = sum(q["chars_total"] for q in reqs)
    obs_chars = sum(q["chars_by_role"].get("observation", 0) for q in reqs)
    role_tot = Counter()
    for q in reqs:
        role_tot.update(q["chars_by_role"])
    print("\nrequest composition (chars over all %d action requests): total %d" % (len(reqs), tot))
    for k in ("chars_system", "chars_task", "chars_status"):
        v = sum(q[k] for q in reqs)
        print(f"  {k[6:]}: {v} ({100 * v / tot:.1f}%)")
    for k, v in role_tot.most_common():
        print(f"  entries/{k}: {v} ({100 * v / tot:.1f}%)")
    toks = sum(q["tokens_exact"] for q in reqs)
    print("exact input tokens: %d (uncached %d, cache_read %d, cache_write %d)" % (toks, sum(q["uncached"] for q in reqs), sum(q["cache_read"] for q in reqs), sum(q["cache_write"] for q in reqs)))
    # cache-aware cost attributable to observation text (estimate)
    cost_obs = 0.0
    for r in runs:
        reqs_r = r["requests"]
        cpt = sum(q["chars_total"] for q in reqs_r) / max(1, sum(q["tokens_exact"] for q in reqs_r))
        for o in r["observations"]:
            if not o["in_next_request"]:
                continue
            t = o["observation_chars"] / cpt
            cost_obs += t * (PRICE["cache_write_5m"] + PRICE["cache_read"] * max(0, o["requests_resident"] - 1)) / 1e6
    total_cost = sum(r["cost_usd"] for r in runs)
    print("estimated input cost of observation text: USD %.4f over 12 runs (%.1f%% of total run cost USD %.4f)" % (cost_obs, 100 * cost_obs / total_cost, total_cost))
    extras(runs)


def line_kind(line: str) -> str:
    """Exploratory line classes (the generator's fixed background noise is named explicitly)."""
    if "slow query" in line:
        return "WARN slow query (background noise)"
    if re.search(r"\bINFO\b", line):
        return "INFO routine (background noise)"
    if re.search(r"\bERROR\b", line):
        return "ERROR"
    if re.search(r"\bWARN\b", line):
        return "WARN other"
    if line.strip().startswith("- ") or "Thread" in line or "CHG-" in line or "Follow-up" in line:
        return "board/change line"
    if not line.strip():
        return "blank"
    return "other (headers, counts, listings, code output)"


def extras(runs: list[dict]) -> None:
    kinds: Counter = Counter()
    saving = 0.0
    opens = rereads = 0
    for r in runs:
        rd = next(p for p in RUNS if p.name == r["run"])
        ev = [json.loads(x) for x in (rd / "events.jsonl").read_text().splitlines()]
        out = {e["step"]: e["stdout"] or "" for e in ev if e["event"] == "execution_result"}
        cpt = sum(q["chars_total"] for q in r["requests"]) / sum(q["tokens_exact"] for q in r["requests"])
        seen: set[str] = set()
        for o in r["observations"]:
            code = (rd / "scripts" / f"step-{o['step']:03d}.py").read_text()
            files = set(re.findall(r"round-\d\d/(?:logs/)?[\w.-]+\.(?:log|md)", code))
            opens += len(files)
            rereads += len(files & seen)
            seen |= files
            if o["retained_chars"] < 2000:
                continue
            noise = 0
            for line in out[o["step"]].splitlines():
                k = line_kind(line)
                kinds[k] += len(line) + 1
                if "background noise" in k:
                    noise += len(line) + 1
            saving += noise / cpt * (PRICE["cache_write_5m"] + PRICE["cache_read"] * max(0, o["requests_resident"] - 1)) / 1e6
    tot = sum(kinds.values())
    print("\nline classes in observations >= 2000 chars (chars):")
    for k, v in kinds.most_common():
        print(f"  {k}: {v} ({100 * v / tot:.0f}%)")
    print("residence (later requests still holding the observation):", sorted(Counter(o["requests_resident"] for r in runs for o in r["observations"]).items()))
    print(f"explicit fixture-file references in code: {opens}, of which reread after an earlier step: {rereads}")
    total_cost = sum(r["cost_usd"] for r in runs)
    print("upper-bound input saving if every background-noise line in observations >= 2000 chars vanished "
          f"(cache-aware estimate): USD {saving:.4f} over 12 runs, USD {saving / 12:.4f} per run "
          f"({100 * saving / total_cost:.1f}% of mean run cost USD {total_cost / 12:.4f}); Jev cost and risk not included")
    ev_kinds: Counter = Counter()
    for task in sorted({r["task"] for r in runs}):
        run = next(p for p in RUNS if f"-{task}-" in p.name)
        truth = json.loads((run / "evaluator" / "truth.json").read_text())
        for inc in truth["incidents"]:
            for refs in inc["evidence_groups"].values():
                for path, n in refs:
                    line = (ART / "fixtures" / task / path).read_text().splitlines()[n - 1]
                    k = "board/change file" if path.endswith(".md") else line_kind(line)
                    if k.startswith("other") and '"level"' in line:
                        k = "JSON-format log line"
                    ev_kinds[k] += 1
    print("scorer evidence lines by class (check only, never a filter input):", dict(ev_kinds))


if __name__ == "__main__":
    main()
