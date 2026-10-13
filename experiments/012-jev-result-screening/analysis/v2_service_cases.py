"""012 v2 (document service): offline opportunity check and compatibility-diagnostic cases.

Run with the clm-lib environment, from this folder:
    uv run --project <path to clm-lib> python v2_service_cases.py opportunity
    uv run --project <path to clm-lib> python v2_service_cases.py build   # screen-cases-v2.json

The same query templates and label scheme as v1 (`screen_cases.py`): for each question, a
*specific* and a *short* query at the default k=5, run through the host-side `DocService`.
Labels come from generator truth, before any Jev answer: `support` (in a valid support set),
`context` (same subject, in no support set), `irrelevant` (other subjects, the related-budgets
distractor, general documents).
"""

from __future__ import annotations

import hashlib
import json
import statistics
import sys
from pathlib import Path

from clm_lib.docservice import DOMAINS, DocService
from clm_lib.jev_screen import eligible, parse_blocks
from clm_lib.tasks import generate

HERE = Path(__file__).resolve().parent
PILOT = ["docsvc-dev-1", "docsvc-dev-2"]
DIAG = ["docsvc-diag-1", "docsvc-diag-2", "docsvc-diag-3"]


def queries(q: dict) -> list[tuple[str, str]]:
    s = DOMAINS[q["domain"]]
    situation = {
        "current": s["base_q"],
        "past": s["base_q"] + " " + q["text"].rsplit(" on ", 1)[-1].rstrip("?"),
        "exception": s["group_q"],
        "carveout": s["sub_q"],
        "additive": s["cond_q"],
    }[q["type"]]
    return [("specific", f"{s['quantity']} {situation}"), ("short", s["quantity"])]


def label(q: dict, pid: str) -> str:
    if any(pid in st for st in q["support_sets"]):
        return "support"
    f = q["facts"]
    doc, sec = pid.split(" §")
    if doc in (f["p"], f["old"], f["memo"]) or (doc == f["faq"] and int(sec) == f["faq_sec"]):
        return "context"
    return "irrelevant"


def block_for(svc: DocService, query: str, k: int = 5) -> str:
    hits = svc.search(query, k)
    lines = [f'<<search-result SR-001 query="{query}" k={k} returned={len(hits)} saved=/task/workspace/search-results/SR-001.txt>>']
    for p in hits:
        lines += [svc.header(p), p["text"]]
    lines.append("<<end search-result SR-001>>")
    return "\n".join(lines) + "\n"


def cases_for(name: str, split: str) -> list[dict]:
    inst = generate(name)
    svc = DocService(inst.truth.corpus)
    out = []
    for q in inst.truth.questions:
        for kind, query in queries(q):
            b = parse_blocks(block_for(svc, query))[0]
            labels = {p["id"]: label(q, p["id"]) for p in b.passages}
            out.append(
                {
                    "id": f"{name}:{q['qid']}:{kind}", "split": split, "instance": name,
                    "question": q["qid"], "qtype": q["type"], "query_kind": kind, "task": inst.prompt,
                    "query": b.query,
                    "intent": f"Find the {DOMAINS[q['domain']]['quantity']} that applies to: {q['text']}",
                    "passages": b.passages, "eligible": eligible(b), "labels": labels,
                    "support_sets_present": [st for st in q["support_sets"] if all(x in labels for x in st)],
                    "support_sets": q["support_sets"],
                }
            )
    return out


def opportunity() -> None:
    for group, names in (("pilot dev (docsvc-dev-1/2)", PILOT), ("compatibility diagnostic (docsvc-diag-1..3)", DIAG)):
        cases = [c for n in names for c in cases_for(n, group)]
        el = [c for c in cases if c["eligible"]]
        chars = {"support": 0, "context": 0, "irrelevant": 0}
        for c in el:
            for p in c["passages"]:
                chars[c["labels"][p["id"]]] += len(p["header"]) + len(p["text"]) + 2
        tot = sum(chars.values()) or 1
        sizes = [sum(len(p["header"]) + len(p["text"]) + 2 for p in c["passages"]) for c in cases]
        ptext = [len(p["text"]) for c in cases for p in c["passages"]]
        qs = {(c["instance"], c["question"]) for c in cases}
        qel = {(c["instance"], c["question"]) for c in el}
        print(f"== {group}: {len(qs)} questions, {len(cases)} ordinary queries at k=5")
        print(f"   result size (chars): median {statistics.median(sizes):.0f}, min {min(sizes)}, max {max(sizes)}; passage text median {statistics.median(ptext):.0f}")
        print(f"   eligible results: {len(el)}/{len(cases)}; questions with an eligible result: {len(qel)}/{len(qs)}")
        print("   by query kind: " + ", ".join(f"{k} {sum(1 for c in el if c['query_kind'] == k)}/{sum(1 for c in cases if c['query_kind'] == k)}" for k in ("specific", "short")))
        print(f"   results holding a complete support set: {sum(1 for c in cases if c['support_sets_present'])}/{len(cases)}")
        print("   eligible chars by label: " + ", ".join(f"{k} {v} ({100 * v / tot:.0f}%)" for k, v in chars.items()))
        print(f"   irrelevant passages per eligible result: mean {sum(sum(1 for v in c['labels'].values() if v == 'irrelevant') for c in el) / max(1, len(el)):.1f}")


def build() -> None:
    cases = [c for n in DIAG for c in cases_for(n, "frozen")]
    doc = {
        "version": "jev-screen-diag/1",
        "screen_version": "result-screen/1",
        "workload": "docsvc-gen/1 (document service)",
        "labelled": "2026-10-13, from generator truth, before any Jev answer; author-checked, not independently validated",
        "cases": cases,
    }
    out = HERE.parent / "screen-cases-v2-service.json"
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(out.name, hashlib.sha256(out.read_bytes()).hexdigest(), len(cases), "cases", sum(c["eligible"] for c in cases), "eligible")


if __name__ == "__main__":
    {"opportunity": opportunity, "build": build}[sys.argv[1]]()
