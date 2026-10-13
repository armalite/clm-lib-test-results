"""012 v2 development pilot (document service): table, means and evaluator-only checks.

Usage (from this folder):  python v2_pilot_table.py
Reads only the exported artifacts (no clm-lib import, no API calls). The comparison of
omitted passages with the support sets in each run's `evaluator/truth.json` is evaluator-only
analysis after the run; it was never an input to screening.
"""

from __future__ import annotations

import json
from pathlib import Path

ART = Path(__file__).resolve().parent.parent / "artifacts"
COMP = json.loads((ART / "comparisons" / "20261013T081314" / "20261013T081314.json").read_text())
RUNS = ART / "runs" / "v2" / "calibration"


def main() -> None:
    per: dict[str, list[dict]] = {"A": [], "B": []}
    for cell in COMP["cells"]:
        run = RUNS / cell["run_id"]
        m = json.loads((run / "summary.json").read_text())
        truth = json.loads((run / "evaluator" / "truth.json").read_text())
        support = {pid for q in truth["questions"] for st in q["support_sets"] for pid in st}
        rs, sv, u, c = m["result_screen"], m["result_screen"]["service"], m["usage_provider_reported"], m["counts"]
        cond = "B" if rs["mode"] == "jev" else "A"
        omitted = [i for b in rs["block_log"] for i in (b.get("omitted") or [])]
        ev = [json.loads(x) for x in (run / "events.jsonl").read_text().splitlines()]
        explicit = set()
        for e in ev:
            if e["event"] == "response":
                a = json.loads(e["text"])
                if a.get("action") == "fetch":
                    explicit |= {i for i in a["ids"] if i in omitted}
        row = dict(
            task=m["task"], cond=cond, position=cell["position"], strict=m["score"]["strict_success"],
            passed=f"{m['score']['passed']}/{m['score']['checks']}", unsupported=m["score"]["unsupported_citations"],
            anthropic=m["cost"]["by_provider"]["anthropic"], typesafe=m["cost"]["by_provider"]["typesafe"],
            elapsed=m["elapsed_s"], calls=c["provider_calls"], executions=c["executions"],
            searches=sv["searches"], fetches=sv["fetches"], fetched_ids=sv["fetched_ids"],
            uncached=u["input_tokens_uncached"], cache_read=u["cache_read_input_tokens"],
            cache_write=u["cache_creation_input_tokens"], output=u["output_tokens"],
            edits=c["edits_accepted_changed"],
            edit_steps=[e["step"] for e in ev if e["event"] == "context_edit" and e.get("changed")],
            eligible=rs["eligible"], screened=rs["screened"], chars_screened=rs["chars_screened"],
            chars_kept=rs["chars_kept"], notice_chars=rs["notice_chars"], passages_omitted=len(omitted),
            omitted_in_support_set=sorted(i for i in omitted if i in support),
            omitted_fetched_by_id=len(explicit),
            omitted_recovered_any_fetch=len(sv["fetch_omitted_recovered"]),
            errors=rs["errors"], jev_attempts=m["jev"]["attempts"], jev_latency_s=m["jev"]["latency_s"],
        )
        per[cond].append(row)
        print(json.dumps(row))
    for cond, rows in per.items():
        n = len(rows)
        avg = lambda k: sum(r[k] for r in rows) / n  # noqa: E731
        print(
            f"{cond} (mean of {n}): strict {sum(r['strict'] for r in rows)}/{n}; USD "
            f"{sum(r['anthropic'] + r['typesafe'] for r in rows) / n:.6f} (TypeSafe {avg('typesafe'):.6f}); "
            f"elapsed {avg('elapsed'):.1f} s; calls {avg('calls'):.1f}; searches {avg('searches'):.1f}; "
            f"fetches {avg('fetches'):.1f}; cache_read {avg('cache_read'):.0f}; cache_write {avg('cache_write'):.0f}; "
            f"uncached {avg('uncached'):.0f}; output {avg('output'):.0f}"
        )


if __name__ == "__main__":
    main()
