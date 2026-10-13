"""Experiment 011 agent pilot: tables and step accounting from the exported artifacts.

Usage (from this folder):  python pilot_analysis.py [--verdicts]

Reads only ../artifacts (comparison record and pilot runs); no clm-lib import, no API calls.
Prints the per-run table, per-condition means, a step-type breakdown of model calls and cost
(confirmations, revisions, proposing steps, code steps, requirement rereads, other), the
intervention coverage (proposals, checks, recovery bypasses) and a mechanical screen of
requirement terms dropped from the context at each applied edit. Jev's verdicts are printed
only with ``--verdicts`` (the screen was reviewed before they were read; see
pilot-edit-review.md for the disclosed exception).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ART = Path(__file__).resolve().parent.parent / "artifacts"
COMPARISON = ART / "comparisons" / "20261013T045649" / "20261013T045649.json"
RUNS = ART / "runs" / "pilot" / "calibration"
COND = {"off": "A", "control": "B", "jev": "C"}
TERMS = {
    "FORMAT": ["json"],
    "PERM": ["viewer", "permissionerror"],
    "STATUS": ["include_archived"],
    "CONF": ["audit"],
    "SINCE": ["since"],
    "OBLIG": ["exported_by"],
    "LIMIT": ["max_records", "truncated"],
}
PARTIAL = {"PERM": ["owner"], "STATUS": ["admin"]}


def load(run: Path) -> tuple[dict, list[dict], dict]:
    m = json.loads((run / "summary.json").read_text())
    ev = [json.loads(x) for x in (run / "events.jsonl").read_text().splitlines()]
    truth = json.loads((run / "evaluator" / "truth.json").read_text())
    return m, ev, truth


def config_at(schedule: list, stage: int) -> dict:
    cfg: dict = {}
    for changes in schedule[:stage]:
        for module, version in changes:
            cfg[module] = version
    return cfg


def step_types(m: dict, ev: list[dict], run: Path) -> dict[int, str]:
    """One label per model step (a step's repairs share its label)."""
    actions = {t["step"]: t.get("action") for t in m["management"]["timeline"]}
    ec = m["edit_check"]
    proposing = {p["step"]: p for p in ec["proposal_log"] if not p["id"].startswith("R")}
    edits = {e["step"] for e in ev if e["event"] == "context_edit" and e.get("changed")}
    code = {e["step"] for e in ev if e["event"] == "workspace_changes" and e["changed"]}
    scripts = {e["step"]: (run / e["script"]).read_text() for e in ev if e["event"] == "execution_start"}
    out = {}
    for step, act in actions.items():
        if act == "confirm_edit":
            out[step] = "confirm"
        elif act in ("advance", "final"):
            out[step] = act
        elif step in proposing and proposing[step].get("replaces"):
            out[step] = "revision"
        elif step in proposing or (ec["mode"] == "off" and step in edits):
            out[step] = "context write" + (" + code" if step in code else "")
        elif step in code:
            out[step] = "code"
        elif "REQUIREMENTS.md" in scripts.get(step, ""):
            out[step] = "requirement reread"
        else:
            out[step] = "other execute (tests, inspection)"
    return out


def step_costs(ev: list[dict]) -> dict[int, float]:
    cost: dict[int, float] = {}
    for e in ev:
        if e["event"] == "response":
            cost[e["step"]] = cost.get(e["step"], 0.0) + e["ledger_charged_usd"]
    return cost


def edit_screen(m: dict, ev: list[dict], truth: dict, run: Path) -> list[dict]:
    revs = {
        json.loads(p.read_text())["number"]: json.loads(p.read_text())["entries"]
        for p in (run / "context").glob("rev-*.json")
    }
    stage, stage_at = 1, {}
    for e in ev:
        if e["event"] == "stage_released":
            stage = e["stage"]
        if "step" in e:
            stage_at.setdefault(e["step"], stage)
    rows = []
    for e in ev:
        if e["event"] != "context_edit" or not e.get("changed"):
            continue
        before = "\n".join(x["body"] for x in revs[e["before_revision"]]).lower()
        after = "\n".join(x["body"] for x in revs[e["after_revision"]]).lower()
        cfg = config_at(truth["schedule"], stage_at[e["step"]])
        dropped = []
        for module, version in cfg.items():
            if module == "FORMAT" and version == 1:
                continue
            for t in TERMS[module] + (PARTIAL.get(module, []) if version > 1 else []):
                if t in before and t not in after:
                    dropped.append(f"{module}:{t}")
        rows.append({"step": e["step"], "stage": stage_at[e["step"]], "dropped_terms": dropped})
    return rows


def main() -> None:
    show = "--verdicts" in sys.argv
    comp = json.loads(COMPARISON.read_text())
    per: dict[str, list[dict]] = {"A": [], "B": [], "C": []}
    for cell in comp["cells"]:
        run = RUNS / cell["run_id"]
        m, ev, truth = load(run)
        s, ec, u = m["score"], m["edit_check"], m["usage_provider_reported"]
        cond = COND[ec["mode"]]
        types = step_types(m, ev, run)
        costs = step_costs(ev)
        by_type: dict[str, list[float]] = {}
        for step, t in types.items():
            by_type.setdefault(t, []).append(costs.get(step, 0.0))
        rec = {
            "task": m["task"],
            "cond": cond,
            "position": cell["position"],
            "strict": s["strict_success"],
            "passed": f"{s['passed']}/{s['checks']}",
            "anthropic": m["cost"]["by_provider"]["anthropic"],
            "typesafe": m["cost"]["by_provider"]["typesafe"],
            "elapsed": m["elapsed_s"],
            "calls": m["counts"]["provider_calls"],
            "repairs": m["counts"]["repair_calls"],
            "api_retries": m["counts"]["api_retries"],
            "edits": m["counts"]["edits_accepted_changed"],
            "proposals": ec["proposals"],
            "by_status": ec["proposals_by_status"],
            "confirms": ec["confirm_actions"],
            "checks": ec["checks"],
            "verdicts": ec["verdicts"],
            "recovery_requests": m["counts"]["recovery_requests"],
            "recovery_exempt": ec["recovery_exempt_edits"],
            "pressure_steps": m["counts"]["pressure_steps"],
            "req_reads": ec["requirement_reads"],
            "tokens": {
                "uncached_in": u["input_tokens_uncached"],
                "cache_read": u["cache_read_input_tokens"],
                "cache_write": u["cache_creation_input_tokens"],
                "out": u["output_tokens"],
            },
            "jev_tokens": m["jev"]["usage_typesafe_tokens"],
            "jev_latency_s": m["jev"]["latency_s"],
            "steps_by_type": {t: (len(v), round(sum(v), 6)) for t, v in sorted(by_type.items())},
            "screen": edit_screen(m, ev, truth, run),
        }
        per[cond].append(rec)
        print(f"\n== {rec['task']} {cond} (position {rec['position']})")
        for k, v in rec.items():
            if k in ("verdicts",) and not show:
                continue
            if k not in ("task", "cond", "position"):
                print(f"   {k}: {v}")
        if show and ec["mode"] == "jev":
            for p in ec["proposal_log"]:
                print(f"   {p['id']} {p['status']} {p['check']['verdict']} {p['check']['answers']}")
    print("\n== per-condition means (2 runs each)")
    for cond, rs in per.items():
        n = len(rs)
        print(
            f"   {cond}: strict {sum(r['strict'] for r in rs)}/{n}; mean USD "
            f"{sum(r['anthropic'] + r['typesafe'] for r in rs) / n:.6f} (Anthropic "
            f"{sum(r['anthropic'] for r in rs) / n:.6f}, TypeSafe {sum(r['typesafe'] for r in rs) / n:.6f}); "
            f"mean elapsed {sum(r['elapsed'] for r in rs) / n:.1f} s; mean calls "
            f"{sum(r['calls'] for r in rs) / n:.1f}"
        )


if __name__ == "__main__":
    main()
