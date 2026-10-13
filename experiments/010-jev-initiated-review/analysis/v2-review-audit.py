"""Offline audit of experiment 010 v2 reviews (read-only; exploratory classification).

Usage (from a clm-lib checkout with the raw runs): python v2-review-audit.py <runs dir> <out dir>
"""

import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path

from clm_lib.tasks import generate
from clm_lib.update_review import build_payload

RUNS = Path(sys.argv[1])
comp = json.load(open(RUNS / "comparisons" / "20261012T213922.json"))
CODE = re.compile(r"\b(?:[A-Z][A-Z_]{4,}|CHG-\d+)\b")  # cause/follow-up codes and change ids
STATUS = re.compile(r"\b(ongoing|mitigated|resolved|false alarm|closed|open|revised)\b", re.I)


def notes(entries):
    return " ".join(e["body"] for e in entries if e["role"] in ("note", "summary"))


out = []
for c in comp["cells"]:
    if c["mode"] == "clm_helpers":
        continue
    rid = c["run_id"]
    R = RUNS / rid
    m = json.load(open(R / "summary.json"))
    inst = generate(c["task"])
    revs = {json.load(open(p))["number"]: json.load(open(p)) for p in glob.glob(f"{R}/context/rev-*.json")}
    ev = [json.loads(x) for x in open(R / "events.jsonl")]
    resp = {}
    for e in ev:
        if e["event"] == "response" and e.get("kind") == "action":
            try:
                resp[e["step"]] = json.loads(e["text"])
            except Exception:
                pass
    edits = {e["step"]: e for e in ev if e["event"] == "context_edit" and e.get("changed")}
    ir = m["initiated_review"]
    for rec in [r for r in ir["records"]]:
        stage = rec["stage"]
        payload = build_payload(inst.stages[stage - 1], 4000)[0]
        es = rec.get("authorised_edit_step")
        row = {
            "run": rid,
            "task": c["task"],
            "cond": "C" if c["mode"].endswith("jev") else "B",
            "review_step": rec["step"],
            "stage": stage,
            "stages_total": rec["stages_total"],
            "purpose": rec["purpose"],
            "status": rec["status"],
            "jev_skip_reason": (
                "B: no Jev by design"
                if not c["mode"].endswith("jev")
                else "compaction purpose -> not_applicable" if rec["status"] == "not_applicable" else rec["status"]
            ),
            "candidates": len(rec["candidate_ids"]),
            "candidate_notes": sum(1 for i in rec["candidate_ids"] if not i.startswith("s")),
            "latest_round": stage,
            "latest_payload_lines": len(payload.splitlines()),
            "latest_payload_has_status_or_cause_change": bool(
                re.search(r"status:|root cause revised|opened|closed|Follow-up", payload)
            ),
            "edit_step": es,
            "thought": (resp.get(es, {}) or {}).get("thought", "")[:160] if es else None,
        }
        if es and es in edits:
            e = edits[es]
            before, after = revs[e["before_revision"]]["entries"], revs[e["after_revision"]]["entries"]
            nb, na = notes(before), notes(after)
            new_codes = sorted(set(CODE.findall(na)) - set(CODE.findall(nb)))
            pay_codes = set(CODE.findall(payload))
            row.update(
                removed=len(e["removed"]),
                added=len(e["added"]),
                rewritten=len(e["rewritten"]),
                chars_before=e["chars_before"],
                chars_after=e["chars_after"],
                note_chars_before=len(nb),
                note_chars_after=len(na),
                new_codes_in_notes=new_codes[:12],
                new_codes_from_latest_payload=sorted(set(new_codes) & pay_codes),
                new_round_tag=bool(re.search(rf"\bR{stage}\b|round-{stage:02d}", na) and not re.search(rf"\bR{stage}\b|round-{stage:02d}", nb)),
            )
            # Exploratory classification of the edit content.
            grew_notes = len(na) > len(nb)
            if not grew_notes and not new_codes and not row["new_round_tag"]:
                cls = "pure compaction (notes not extended)"
            elif row["new_codes_from_latest_payload"] or row["new_round_tag"]:
                cls = "incorporated newly released findings"
            else:
                cls = "extended notes (other content)"
            row["exploratory_class"] = cls
        out.append(row)

json.dump(out, open(Path(sys.argv[2]) / "v2-review-audit.json", "w"), indent=1)
print("reviews audited:", len(out))
print("by condition/purpose/status:", Counter((r["cond"], r["purpose"], r["status"]) for r in out))
print("skip reasons:", Counter(r["jev_skip_reason"] for r in out))
print("reviews with >=1 candidate:", sum(r["candidates"] > 0 for r in out), "with >=1 note candidate:", sum(r["candidate_notes"] > 0 for r in out))
print("latest payload non-empty:", sum(r["latest_payload_lines"] > 0 for r in out), "| with status/cause/follow-up change lines:", sum(r["latest_payload_has_status_or_cause_change"] for r in out))
print("before last stage:", sum(r["stage"] < r["stages_total"] for r in out))
print("exploratory edit classes:", Counter(r.get("exploratory_class") for r in out))
print("same latest round reviewed more than once (run, round):", sum(1 for k, v in Counter((r["run"], r["stage"]) for r in out).items() if v > 1))
