"""014 development revision R1: the configured delegation smoke on w3-smoke-1.

Usage (from this folder):  python r1_smoke.py
Reads only the exported run and the offline replay output in ./replay-r1/ (written by
`clm-lib replay-jev`, jev-replay/2; sandboxed re-execution with scripted answers, no API calls).
No clm-lib import, no API calls. Prints the run metrics, the replay classes per Jev-using
execution (frozen variants and the post-hoc last-request diagnostic, kept apart), and the
correctness of each Jev-governed selection against the evaluator truth (after the run).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN_ID = "20261014T020047-clm_helpers-cacheon-jprim-w3-smoke-1-5bae"
RUN = HERE.parent / "artifacts" / "runs" / "r1-smoke" / "smoke" / RUN_ID
REPLAY = HERE / "replay-r1" / RUN_ID / "replay.json"


def main() -> None:
    m = json.loads((RUN / "summary.json").read_text())
    u, c = m["usage_provider_reported"], m["counts"]
    print(json.dumps({
        "code": f"{m['score']['passed']}/{m['score']['checks']}", "strict": m["score"]["strict_success"],
        "register_harm": m["register"]["harm"], "register_history_errors": m["register"]["history_errors"],
        "register_incomplete": m["register"]["incomplete"], "usd": m["cost"]["incurred_usd"],
        "by_provider": m["cost"]["by_provider"], "elapsed_s": m["elapsed_s"], "calls": c["provider_calls"],
        "repairs": c["repair_calls"], "retries": c["api_retries"], "executions": c["executions"],
        "edits": c["edits_accepted_changed"], "pressure_steps": c["pressure_steps"], "tokens": u,
        "peak_request_est": m["peak_request_tokens_est"], "jev_calls": m["jev_primitive"]["calls"],
        "jev_items": m["jev_primitive"]["items"], "jev_latency_s": m["jev"]["latency_s"],
        "jev_errors": m["jev"]["errors"], "helpers": m["helpers"]["created"],
    }))
    rp = json.loads(REPLAY.read_text())
    print("frozen criterion: stages substantive under a valid substitution:", rp["stages_substantive_under_valid_substitution"])
    print("post-hoc diagnostic (not used for the verdict): stages substantive under last-request substitution:",
          rp["post_hoc_stages_substantive_last_request"])
    for s in rp["steps"]:
        print(f"  step {s['step']} stage {s['stage']}: reproduced={s['reproduced']} withheld={s['dependence']['class']} "
              f"frozen={ {k: v['class'] for k, v in s['substitutions'].items()} } "
              f"post_hoc={ {k: v['class'] for k, v in s['post_hoc_last_request'].items()} } caller_audit={s['audit']['caller']}")
    # Jev-governed selections vs truth (evaluator-only, after the run). The helper prints
    # "<new id> -> [<amended entry ids>]" per new item; its request background holds the item text.
    truth = json.loads((RUN / "evaluator" / "truth.json").read_text())
    text = {i["id"]: " ".join(i["text"].split()) for i in truth["items"]}
    affects = {n: {e["target"] for e in effs if e["effect"] != "none"} for n, effs in truth["effects"].items()}
    prim = [json.loads(p.read_text()) for p in sorted((RUN / "jev_primitive").glob("*.json"))]
    ev = [json.loads(x) for x in (RUN / "events.jsonl").read_text().splitlines()]
    tot = {"correct_amend": 0, "false_amend": 0, "missed": 0, "correct_keep": 0}
    for e in ev:
        if e["event"] != "execution_result":
            continue
        for new, hits in re.findall(r"^(S\d+\.\d+) -> \[(.*?)\]", e.get("stdout") or "", re.M):
            hit = re.findall(r"'([^']+)'", hits)
            req = [p for p in prim if p["step"] == e["step"] and text[new][:60] in p["request"]["background"]]
            if not req:
                continue
            cites = {it["key"]: set(re.findall(r"S\d+\.\d+", it["text"].split("]")[0])) for it in req[0]["request"]["items"]}
            true = affects.get(new, set())
            row = {
                "correct_amend": [h for h in hit if cites[h] & true],
                "false_amend": [h for h in hit if not cites[h] & true],
                "missed": [k for k in cites if k not in hit and cites[k] & true],
            }
            tot["correct_keep"] += sum(1 for k in cites if k not in hit and not cites[k] & true)
            for k, v in row.items():
                tot[k] += len(v)
            print(f"  step {e['step']} {new}: truth {sorted(true)} -> {row}")
    print("selection vs truth:", tot)


if __name__ == "__main__":
    main()
