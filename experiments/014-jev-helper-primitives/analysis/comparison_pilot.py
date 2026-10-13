"""014 comparison phase, W3 development pilot (and the B smoke): table and mechanism evidence.

Usage (from this folder):  python comparison_pilot.py
Reads only the exported artifacts and the replay outputs in ./replay/ (written offline by
`clm-lib replay-jev`, which re-executes Jev-using steps in the sandbox with scripted answers; no
API calls). No clm-lib import, no API calls. Descriptive only: two instances, one run per cell.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE.parent / "artifacts" / "runs"
RUNS = [
    ("smoke", "B", "comparison-smoke/smoke/20261013T143429-clm_helpers-cacheon-jprim-w3-smoke-1-8797"),
    ("w3-dev-1", "A", "comparison-dev/calibration/20261013T143716-clm_helpers-cacheon-w3-dev-1-495e"),
    ("w3-dev-1", "B", "comparison-dev/calibration/20261013T143929-clm_helpers-cacheon-jprim-w3-dev-1-4a83"),
    ("w3-dev-2", "B", "comparison-dev/calibration/20261013T144206-clm_helpers-cacheon-jprim-w3-dev-2-d925"),
    ("w3-dev-2", "A", "comparison-dev/calibration/20261013T144446-clm_helpers-cacheon-w3-dev-2-36fe"),
]
RUNTIME_ID = re.compile(r"^s\d+\.(act|obs|rcpt)$")
EARLIER = re.compile(r"/task/fixtures/stage-0*(\d+)")


def entries(run: Path, rev: int) -> dict[str, str]:
    doc = json.loads((run / "context" / f"rev-{rev:04d}.json").read_text())
    return {e["id"]: e["body"] for e in doc["entries"]}


def row(task: str, cond: str, rel: str) -> dict:
    run = ART / rel
    m = json.loads((run / "summary.json").read_text())
    ev = [json.loads(x) for x in (run / "events.jsonl").read_text().splitlines()]
    s, reg, u, c = m["score"], m["register"], m["usage_provider_reported"], m["counts"]
    snaps = {k: (sum(x["passed"] for x in v["modules"].values()), sum(x["total"] for x in v["modules"].values())) for k, v in s["snapshots"].items()}
    # Model-written context text introduced by accepted edits (non-runtime entries).
    written = 0
    for e in ev:
        if e["event"] == "context_edit" and e.get("status") == "accepted" and e.get("changed"):
            b, a = entries(run, e["before_revision"]), entries(run, e["after_revision"])
            written += sum(len(t) for i, t in a.items() if not RUNTIME_ID.match(i) and b.get(i) != t)
    # Rereads: executions naming an earlier stage folder than the latest released one.
    latest, rereads = 1, 0
    for e in ev:
        if e["event"] == "stage_released":
            latest = e["stage"]
        elif e["event"] == "execution_start":
            code = (run / e["script"]).read_text()
            rereads += any(int(n) < latest for n in EARLIER.findall(code))
    jp = m["jev_primitive"]
    rp = HERE / "replay" / run.name / "replay.json"
    replay = json.loads(rp.read_text()) if rp.exists() else None
    printed = sum(
        1
        for e in ev
        if e["event"] == "execution_result"
        and e["step"] in (jp.get("steps_with_calls") or [])
        and re.search(r"JEV FLAG|\{'S\d|\{'\d+'", e.get("stdout") or "")
    )
    return {
        "task": task,
        "cond": cond,
        "run_id": run.name,
        "code": f"{s['passed']}/{s['checks']}",
        "strict": s["strict_success"],
        "stale_code": s["stale"],
        "snapshots_failed": {k: f"{p}/{t}" for k, (p, t) in snaps.items() if p < t},
        "register_harm": reg["harm"],
        "register_history_errors": reg["history_errors"],
        "register_incomplete": reg["incomplete"],
        "register_missing_stages": reg["missing_stages"],
        "usd": m["cost"]["incurred_usd"],
        "anthropic": m["cost"]["by_provider"]["anthropic"],
        "typesafe": m["cost"]["by_provider"]["typesafe"],
        "elapsed_s": m["elapsed_s"],
        "calls": c["provider_calls"],
        "repairs": c["repair_calls"],
        "api_retries": c["api_retries"],
        "executions": c["executions"],
        "edits": c["edits_accepted_changed"],
        "pressure_steps": c["pressure_steps"],
        "uncached": u["input_tokens_uncached"],
        "cache_read": u["cache_read_input_tokens"],
        "cache_write": u["cache_creation_input_tokens"],
        "output": u["output_tokens"],
        "peak_request_est": m["peak_request_tokens_est"],
        "helpers_created": m["helpers"]["created"],
        "jev_requests": jp.get("requests", 0),
        "jev_calls": jp.get("calls", 0),
        "jev_items": jp.get("items", 0),
        "jev_steps": jp.get("steps_with_calls", []),
        "jev_errors": m["jev"]["errors"],
        "jev_latency_s": m["jev"]["latency_s"],
        "replay": replay["summary"] if replay else None,
        "replay_reproduced": all(x["reproduced"] for x in replay["steps"]) if replay else None,
        "jev_steps_printing_answers": printed,
        "model_written_context_chars": written,
        "executions_rereading_earlier_stages": rereads,
    }


IDS = re.compile(r"S\d+\.\d+")


def jev_quality(rel: str) -> dict:
    """Evaluator-only, after the run: Jev's answers at 0.5 against the item effects. A judged
    pair is (notice item named in the request, register item named by the submitted key or
    text); it is truly affected if the notice item replaces, amends, withdraws or activates it."""
    run = ART / rel
    truth = json.loads((run / "evaluator" / "truth.json").read_text())
    affects = {n: {e["target"] for e in effs if e["effect"] != "none"} for n, effs in truth["effects"].items()}
    tp = fp = fn = tn = unmapped = 0
    for f in sorted((run / "jev_primitive").glob("*.json")):
        r = json.loads(f.read_text())
        if r.get("status") != "ok":
            continue
        q = r["request"]
        news = IDS.findall(q.get("background", "")) or IDS.findall(q["question"])
        if len(set(news)) != 1:
            unmapped += len(q["items"])
            continue
        new = news[0]
        for it in q["items"]:
            own = IDS.findall(it["key"]) or IDS.findall(it["text"])
            p = r["answers"].get(it["key"])
            if not own or p is None:
                unmapped += 1
                continue
            hit, true = p >= 0.5, any(o in affects.get(new, set()) for o in own)
            tp += hit and true
            fp += hit and not true
            fn += (not hit) and true
            tn += (not hit) and not true
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn, "unmapped_items": unmapped}


def main() -> None:
    rows = [row(*r) for r in RUNS]
    for r in rows:
        print(json.dumps(r))
    for task, cond, rel in RUNS:
        if cond == "B":
            print(f"jev judgments vs truth ({task} B, threshold 0.5): {jev_quality(rel)}")
    pilot = [r for r in rows if r["task"] != "smoke"]
    for task in ("w3-dev-1", "w3-dev-2"):
        a = next(r for r in pilot if r["task"] == task and r["cond"] == "A")
        b = next(r for r in pilot if r["task"] == task and r["cond"] == "B")
        print(
            f"{task}: B-A cost {b['usd'] - a['usd']:+.4f} ({(b['usd'] / a['usd'] - 1):+.0%}), "
            f"time {b['elapsed_s'] - a['elapsed_s']:+.1f} s, calls {b['calls'] - a['calls']:+d}, "
            f"output {b['output'] - a['output']:+d}, cache writes {b['cache_write'] - a['cache_write']:+d}, "
            f"cache reads {b['cache_read'] - a['cache_read']:+d}"
        )


if __name__ == "__main__":
    main()
