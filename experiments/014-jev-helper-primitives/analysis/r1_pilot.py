"""014 R1 matched development pilot (w3-dev-3, w3-dev-4 x A/B): table, means and evidence.

Usage (from this folder):  python r1_pilot.py
Reads only the exported runs and the offline replay outputs in ./replay-r1-pilot/ (written by
`clm-lib replay-jev`, jev-replay/2; sandboxed re-execution with scripted answers, no API calls).
No clm-lib import, no API calls. Descriptive only (two instances, one run per cell).

Definitions (frozen in protocol-r1-pilot.md):
- setup cost: main-model cost of the step whose code first creates a helper module; all other
  steps are maintenance. Total cost, including setup, is the primary efficiency measure;
- register size: lines starting CURRENT / HISTORY in model-written entries of the assessed
  revisions (the register scorer's own parse is in clm-lib; this is a size count only);
- delegation: Jev-using executions reproduced by the recorded replay and `substantive` under the
  last-request intervention (inverted_last or permuted_last); only the decisions of that last
  request are tested by it.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE.parent / "artifacts" / "runs" / "r1-pilot" / "calibration"
RUNS = [
    ("w3-dev-3", "A", "20261014T041357-clm_helpers-cacheon-w3-dev-3-89e5"),
    ("w3-dev-3", "B", "20261014T041616-clm_helpers-cacheon-jprim-w3-dev-3-a692"),
    ("w3-dev-4", "B", "20261014T041952-clm_helpers-cacheon-jprim-w3-dev-4-7abc"),
    ("w3-dev-4", "A", "20261014T042247-clm_helpers-cacheon-w3-dev-4-32ed"),
]
RUNTIME_ID = re.compile(r"^s\d+\.(act|obs|rcpt)$")
EARLIER = re.compile(r"/task/fixtures/stage-0*(\d+)")
IDS = re.compile(r"S\d+\.\d+")


def lines(run: Path, rev: int) -> list[str]:
    doc = json.loads((run / "context" / f"rev-{rev:04d}.json").read_text())
    out = []
    for e in doc["entries"]:
        if not RUNTIME_ID.match(e["id"]):
            out += [ln for ln in e["body"].splitlines() if ln.lstrip(" -*").startswith(("CURRENT", "HISTORY"))]
    return out


def jev_quality(run: Path) -> dict:
    """Evaluator-only, after the run: Jev's answers at 0.5 vs the item effects, by question type
    ("replace" questions vs "modify/affect" questions), where the request's background names the
    new item by its text and the submitted item cites register ids."""
    truth = json.loads((run / "evaluator" / "truth.json").read_text())
    text = {i["id"]: " ".join(i["text"].split()) for i in truth["items"]}
    eff = {n: {e["target"]: e["effect"] for e in v if e["effect"] != "none"} for n, v in truth["effects"].items()}
    out: dict[str, dict[str, int]] = {}
    for f in sorted((run / "jev_primitive").glob("*.json")):
        r = json.loads(f.read_text())
        if r.get("status") != "ok":
            continue
        q = r["request"]
        new = [n for n, t in text.items() if t[:60] in q.get("background", "") or t[:60] in q["question"]]
        if len(new) != 1:
            continue
        kind = "replace" if re.search(r"completely replace|NO part|nothing of the existing", q["question"], re.I) else "modify"
        c = out.setdefault(kind, {"tp": 0, "fp": 0, "fn": 0, "tn": 0})
        for it in q["items"]:
            cited = set(IDS.findall(it["text"].split("]")[0]))
            p = r["answers"].get(it["key"])
            if p is None or not cited:
                continue
            effs = {eff[new[0]].get(x) for x in cited} - {None}
            true = ("replaces" in effs) if kind == "replace" else bool(effs)
            hit = p >= 0.5
            c["tp" if hit and true else "fp" if hit else "fn" if true else "tn"] += 1
    return out


def row(task: str, cond: str, rid: str) -> dict:
    run = ART / rid
    m = json.loads((run / "summary.json").read_text())
    ev = [json.loads(x) for x in (run / "events.jsonl").read_text().splitlines()]
    s, reg, u, c = m["score"], m["register"], m["usage_provider_reported"], m["counts"]
    resp = {e["step"]: e for e in ev if e["event"] == "response"}
    created = m["helpers"]["created"]
    setup_step = min(created.values()) if created else None
    setup = round(resp[setup_step]["cost_usd"], 6) if setup_step in resp else 0.0
    out_text = "\n".join(e.get("stdout") or "" for e in ev if e["event"] == "execution_result")
    latest, rereads = 1, 0
    for e in ev:
        if e["event"] == "stage_released":
            latest = e["stage"]
        elif e["event"] == "execution_start":
            rereads += any(int(n) < latest for n in EARLIER.findall((run / e["script"]).read_text()))
    sizes = []
    for st in reg["stages"]:
        ls = lines(run, st["revision"])
        sizes.append({"stage": st["stage"], "current": sum(1 for x in ls if x.lstrip(" -*").startswith("CURRENT")),
                      "history": sum(1 for x in ls if x.lstrip(" -*").startswith("HISTORY")), "chars": sum(len(x) for x in ls)})
    transient = [(st["stage"], st["harm"], st["history_errors"], st["incomplete"]) for st in reg["stages"]
                 if st["harm"] or st["history_errors"] or st["incomplete"]]
    snaps = {k: f"{sum(x['passed'] for x in v['modules'].values())}/{sum(x['total'] for x in v['modules'].values())}"
             for k, v in s["snapshots"].items() if any(x["passed"] < x["total"] for x in v["modules"].values())}
    jp = m["jev_primitive"]
    rp = HERE / "replay-r1-pilot" / rid / "replay.json"
    replay = json.loads(rp.read_text()) if rp.exists() else None
    return {
        "task": task, "cond": cond, "run_id": rid,
        "code": f"{s['passed']}/{s['checks']}", "strict": s["strict_success"], "snapshot_failures": snaps,
        "register_harm": reg["harm"], "register_history_errors": reg["history_errors"], "register_incomplete": reg["incomplete"],
        "register_stage_errors(stage,harm,hist,incomplete)": transient,
        "usd": m["cost"]["incurred_usd"], "anthropic": m["cost"]["by_provider"]["anthropic"], "typesafe": m["cost"]["by_provider"]["typesafe"],
        "setup_usd": setup, "setup_step": setup_step, "maintenance_usd": round(m["cost"]["incurred_usd"] - setup - m["cost"]["by_provider"]["typesafe"], 6),
        "elapsed_s": m["elapsed_s"], "calls": c["provider_calls"], "repairs": c["repair_calls"], "api_retries": c["api_retries"],
        "executions": c["executions"], "edits": c["edits_accepted_changed"], "pressure_steps": c["pressure_steps"],
        "spills": c["spills"], "recovery_requests": c["recovery_requests"],
        "uncached": u["input_tokens_uncached"], "cache_read": u["cache_read_input_tokens"], "cache_write": u["cache_creation_input_tokens"],
        "output": u["output_tokens"], "peak_request_est": m["peak_request_tokens_est"],
        "helpers_created": created, "helper_revisions": [x for x in m["helpers"]["revised"] if "exporter" not in x["file"]],
        "jev_requests": jp.get("requests", 0), "jev_calls": jp.get("calls", 0), "jev_by_status": jp.get("by_status", {}),
        "jev_items": jp.get("items", 0), "jev_latency_s": m["jev"]["latency_s"],
        "fallback_lines": sum(1 for x in out_text.splitlines() if x.startswith("FALLBACK:")),
        "override_lines": sum(1 for x in out_text.splitlines() if x.startswith("OVERRIDE:")),
        "rereads_of_earlier_stages": rereads,
        "register_size_by_stage": sizes,
        "replay_reproduced": all(x["reproduced"] for x in replay["steps"]) if replay else None,
        "notice_stages_substantive_last_request": [x for x in replay["stages_substantive_last_request"] if x >= 3] if replay else None,
        "last_request_classes": {x["stage"]: {k: v["class"] for k, v in x["last_request"].items()} for x in replay["steps"]} if replay else None,
        "jev_quality": jev_quality(run) if cond == "B" else None,
    }


def main() -> None:
    rows = [row(*r) for r in RUNS]
    for r in rows:
        print(json.dumps(r))
    keys = ("usd", "elapsed_s", "calls", "executions", "edits", "output", "cache_read", "cache_write", "uncached", "jev_calls")
    for cond in ("A", "B"):
        rs = [r for r in rows if r["cond"] == cond]
        print(f"mean {cond} (n=2, descriptive): " + ", ".join(f"{k} {sum(r[k] for r in rs) / 2:.4g}" for k in keys))
    for task in ("w3-dev-3", "w3-dev-4"):
        a = next(r for r in rows if r["task"] == task and r["cond"] == "A")
        b = next(r for r in rows if r["task"] == task and r["cond"] == "B")
        print(f"{task}: B-A cost {b['usd'] - a['usd']:+.4f} ({b['usd'] / a['usd'] - 1:+.1%}), time {b['elapsed_s'] - a['elapsed_s']:+.1f} s, "
              f"calls {b['calls'] - a['calls']:+d}, output {b['output'] - a['output']:+d}, cache writes {b['cache_write'] - a['cache_write']:+d}, "
              f"cache reads {b['cache_read'] - a['cache_read']:+d}")


if __name__ == "__main__":
    main()
