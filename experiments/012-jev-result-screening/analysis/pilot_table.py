"""012 development pilot: per-run table from the exported artifacts (no clm-lib import, no API).

Usage (from this folder):  python pilot_table.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ART = Path(__file__).resolve().parent.parent / "artifacts"
COMP = json.loads((ART / "comparisons" / "20261013T072241" / "20261013T072241.json").read_text())
RUNS = ART / "runs" / "pilot" / "calibration"


def main() -> None:
    per: dict[str, list[dict]] = {"A": [], "B": []}
    for cell in COMP["cells"]:
        run = RUNS / cell["run_id"]
        m = json.loads((run / "summary.json").read_text())
        rs, u, c, s = m["result_screen"], m["usage_provider_reported"], m["counts"], m["score"]
        scripts = sorted((run / "scripts").glob("*.py"))
        calls_search = sum(1 for p in scripts if re.search(r"(?<![.\w])search\(", p.read_text()))
        cond = "B" if rs["mode"] == "jev" else "A"
        row = dict(
            task=m["task"], cond=cond, position=cell["position"], strict=s["strict_success"],
            passed=f"{s['passed']}/{s['checks']}", stale=s["stale"], unsupported=s["unsupported_citations"],
            anthropic=m["cost"]["by_provider"]["anthropic"], typesafe=m["cost"]["by_provider"]["typesafe"],
            elapsed=m["elapsed_s"], calls=c["provider_calls"], executions=c["executions"],
            uncached=u["input_tokens_uncached"], cache_read=u["cache_read_input_tokens"],
            cache_write=u["cache_creation_input_tokens"], output=u["output_tokens"],
            edits=c["edits_accepted_changed"], pressure=c["pressure_steps"], spills=c["spills"],
            steps_calling_search=calls_search, blocks=rs["blocks"], eligible=rs["eligible"],
            screened=rs["screened"], omitted=rs["passages_omitted"], cap_repairs=rs["cap_repairs"],
            show_calls=rs["recovery"]["show_calls"], saved_reads=rs["recovery"]["saved_reads"],
            doc_read_steps=rs["recovery"]["doc_reads"], jev_attempts=m["jev"]["attempts"],
        )
        per[cond].append(row)
        print(json.dumps(row))
    for cond, rows in per.items():
        n = len(rows)
        print(
            f"{cond}: strict {sum(r['strict'] for r in rows)}/{n}; mean USD "
            f"{sum(r['anthropic'] + r['typesafe'] for r in rows) / n:.6f}; mean elapsed "
            f"{sum(r['elapsed'] for r in rows) / n:.1f} s; mean calls {sum(r['calls'] for r in rows) / n:.1f}; "
            f"search blocks {sum(r['blocks'] for r in rows)}; screened {sum(r['screened'] for r in rows)}"
        )


if __name__ == "__main__":
    main()
