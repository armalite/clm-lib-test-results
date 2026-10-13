"""012: ordinary search queries, passage labels and the offline opportunity check (no Jev).

Run with the clm-lib environment, from this folder:
    uv run --project <path to clm-lib> python screen_cases.py opportunity
    uv run --project <path to clm-lib> python screen_cases.py build   # writes screen-cases-v1.json

Queries are mechanical, fixed before any Jev answer: for each question, a *specific* query (the
quantity plus the question's situation) and a *short* query (the quantity alone), at the tool's
documented default k=5. They model ordinary search requests; no large k is used.

Passage labels come from the generator's truth (written before any Jev answer):
- ``support``: in at least one valid support set of the question;
- ``context``: same subject (the policy, its superseded version, its exception memo, or the FAQ
  entry) but in no support set, e.g. a superseded rule for a current-value question or the
  group exception when the question is about the carve-out;
- ``irrelevant``: a different subject, the same-subject "related budgets" distractor, or
  general handbook text.
Context passages are not counted in recall and their omission is reported separately.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import sys
import tempfile
from pathlib import Path

from clm_lib.handbook import DOMAINS, tools_namespace
from clm_lib.jev_screen import eligible, parse_blocks
from clm_lib.tasks import generate

HERE = Path(__file__).resolve().parent
PILOT = ["handbook-dev-1", "handbook-dev-2"]
DIAG_DEV = ["handbook-diag-1"]
DIAG_FROZEN = ["handbook-diag-2", "handbook-diag-3", "handbook-diag-4"]


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


def label(q: dict, pid: str, faq_doc: str) -> str:
    if any(pid in st for st in q["support_sets"]):
        return "support"
    f = q["facts"]
    doc, sec = pid.split(" §")
    if doc in (f["p"], f["old"], f["memo"]) or (doc == faq_doc and int(sec) == f["faq_sec"]):
        return "context"
    return "irrelevant"


def run_search(inst, query: str, k: int = 5) -> str:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "handbook").mkdir()
    for rel, text in inst.files.items():
        if rel.startswith("handbook/"):
            (tmp / rel).write_text(text, encoding="utf-8")
    os.environ["HANDBOOK_FIXTURES"] = str(tmp / "handbook")
    os.environ["HANDBOOK_SAVE_DIR"] = str(tmp / "saved")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        tools_namespace()["search"](query, k)
    return buf.getvalue()


def cases_for(name: str, split: str) -> list[dict]:
    inst = generate(name)
    t = inst.truth
    out = []
    for q in t.questions:
        for kind, query in queries(q):
            b = parse_blocks(run_search(inst, query))[0]
            labels = {p["id"]: label(q, p["id"], t.faq_doc) for p in b.passages}
            present = [st for st in q["support_sets"] if all(x in labels for x in st)]
            out.append(
                {
                    "id": f"{name}:{q['qid']}:{kind}",
                    "split": split,
                    "instance": name,
                    "question": q["qid"],
                    "qtype": q["type"],
                    "query_kind": kind,
                    "task": inst.prompt,
                    "query": b.query,
                    "intent": f"Find the {DOMAINS[q['domain']]['quantity']} that applies to: {q['text']}",
                    "passages": b.passages,
                    "eligible": eligible(b),
                    "labels": labels,
                    "support_sets_present": present,
                    "support_sets": q["support_sets"],
                }
            )
    return out


def opportunity() -> None:
    for group, names in (("pilot dev", PILOT), ("diagnostic", DIAG_DEV + DIAG_FROZEN)):
        cases = [c for n in names for c in cases_for(n, group)]
        el = [c for c in cases if c["eligible"]]
        qs_el = {(c["instance"], c["question"]) for c in el}
        qs = {(c["instance"], c["question"]) for c in cases}
        chars = {"support": 0, "context": 0, "irrelevant": 0}
        for c in el:
            for p in c["passages"]:
                chars[c["labels"][p["id"]]] += len(p["header"]) + len(p["text"]) + 2
        tot = sum(chars.values())
        complete = sum(1 for c in cases if c["support_sets_present"])
        print(f"== {group}: {len(names)} instances, {len(qs)} questions, {len(cases)} queries (k=5)")
        print(f"   eligible results: {len(el)}/{len(cases)}; questions with >= 1 eligible result: {len(qs_el)}/{len(qs)}")
        print(f"   results holding a complete support set: {complete}/{len(cases)}")
        print("   eligible characters by label: " + ", ".join(f"{k} {v} ({100 * v / max(1, tot):.0f}%)" for k, v in chars.items()))
        print(f"   oracle ceiling (omit every irrelevant passage): {100 * chars['irrelevant'] / max(1, tot):.0f}% of eligible characters")
        by = {}
        for c in el:
            by.setdefault(c["query_kind"], []).append(sum(1 for v in c["labels"].values() if v == "irrelevant"))
        print("   irrelevant passages per eligible result:", {k: f"mean {sum(v) / len(v):.1f}" for k, v in by.items()})


def build() -> None:
    cases = [c for n in DIAG_DEV for c in cases_for(n, "dev")] + [c for n in DIAG_FROZEN for c in cases_for(n, "frozen")]
    doc = {
        "version": "jev-screen-diag/1",
        "screen_version": "result-screen/1",
        "labelled": "2026-10-13, from generator truth, before any Jev answer; author-checked, not independently validated",
        "label_meaning": {
            "support": "in at least one valid support set of the question",
            "context": "same subject but in no support set (version, other exception, FAQ entry); not counted in recall",
            "irrelevant": "different subject, the same-subject related-budgets distractor, or general text",
        },
        "cases": cases,
    }
    out = HERE.parent / "screen-cases-v1.json"
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(out.name, hashlib.sha256(out.read_bytes()).hexdigest(), len(cases), "cases")


if __name__ == "__main__":
    {"opportunity": opportunity, "build": build}[sys.argv[1]]()
