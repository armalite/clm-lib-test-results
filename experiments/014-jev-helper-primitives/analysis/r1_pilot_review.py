"""014 R1 matched pilot — retrospective review (EXPLORATORY, after the runs; offline).

Usage (from this folder):  python r1_pilot_review.py
Reads only exported artifacts (no clm-lib import, no API calls). It reconstructs every
judgment-driven register decision made by the two B helpers, pairs it with the question Jev was
asked, the answer, the helper branch and the evaluator truth (item effects), and measures
register growth and the cost of steps by role. Classifications are evaluator-side and
retrospective; they were not part of the frozen pilot analysis.

Decision reconstruction (from each helper's own source, verified against its printed log):
- dev-3 B (reghelper.update, defaults replace_thr=0.7, amend_thr=0.5): per new item, two
  questions about every CURRENT entry, "completely replace…?" (p1) and "conflict with or
  modify…?" (p2); p1 >= 0.7 -> retire to HISTORY, elif p2 >= 0.5 -> append an amendment line;
  the new item is always also added as its own CURRENT entry. The helper prints
  "<new> <entry> <p1> <p2>" for every pair. Its first version (steps 2-3) also asked these
  questions for the initial requirements of stages 1-2.
- dev-4 B (regmaint.update, thr=0.5, rthr=0.75): per new item at stage >= 3, "modify, replace,
  override or withdraw any part…?" about every CURRENT entry (chunks of 20; > 0.5 = hit), then
  "completely replace…?" about the hits (> 0.75 -> retire, else amend in place); a new item
  with hits is not added as its own entry.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE.parent / "artifacts" / "runs" / "r1-pilot" / "calibration"
B3 = "20261014T041616-clm_helpers-cacheon-jprim-w3-dev-3-a692"
B4 = "20261014T041952-clm_helpers-cacheon-jprim-w3-dev-4-7abc"
A3 = "20261014T041357-clm_helpers-cacheon-w3-dev-3-89e5"
A4 = "20261014T042247-clm_helpers-cacheon-w3-dev-4-32ed"
RUNTIME_ID = re.compile(r"^s\d+\.(act|obs|rcpt)$")
CITED = re.compile(r"\[(S\d+\.\d+(?:,\s*S\d+\.\d+)*)\]")
RANK = {"replaces": 4, "amends": 3, "activates": 2, "related": 1, "unrelated": 0}


def load(rid: str) -> tuple[Path, dict, list[dict], list[dict]]:
    run = ART / rid
    truth = json.loads((run / "evaluator" / "truth.json").read_text())
    ev = [json.loads(x) for x in (run / "events.jsonl").read_text().splitlines()]
    prim = [json.loads(p.read_text()) for p in sorted((run / "jev_primitive").glob("*.json"))]
    return run, truth, ev, prim


def relation(truth: dict, new: str, entry_text: str) -> str:
    """The strongest truth relation between a new item and the items an entry cites."""
    cited = {i.strip() for grp in CITED.findall(entry_text) for i in grp.split(",")}
    best = "unrelated"
    for e in truth["effects"].get(new, []):
        if e["target"] in cited:
            rel = "related" if e["effect"] == "none" else e["effect"]
            if RANK[rel] > RANK[best]:
                best = rel
    return best


def classify(rel: str, action: str, initial: bool) -> str:
    if initial and action != "keep":
        return "change questions applied to initial requirements"
    if action == "keep":
        return "missed" if rel in ("replaces", "amends") else "correct keep"
    if action == "retire":
        return {"replaces": "correct retire", "amends": "amendment retired as replacement"}.get(rel, f"retired although {rel}")
    return {
        "amends": "correct amend",
        "replaces": "replacement kept as amendment",
        "activates": "activation recorded as amendment",
        "related": "shared terminology amended",
        "unrelated": "unrelated entry amended",
    }[rel]


def decisions_dev3() -> list[dict]:
    run, truth, ev, prim = load(B3)
    kinds = {i["id"]: i["kind"] for i in truth["items"]}
    text = {i["id"]: " ".join(i["text"].split()) for i in truth["items"]}
    out = []
    for e in ev:
        if e["event"] != "execution_result":
            continue
        for new, ent, p1, p2 in re.findall(r"^(S\d+\.\d+) (reg\.\S+) ([0-9.]+) ([0-9.]+)$", e.get("stdout") or "", re.M):
            p1, p2 = float(p1), float(p2)
            req = next((p for p in prim if p["step"] == e["step"] and text[new][:60] in p["request"]["background"]
                        and ent in p["answers"]), None)
            etext = next((it["text"] for it in req["request"]["items"] if it["key"] == ent), "") if req else ""
            action = "retire" if p1 >= 0.7 else "amend" if p2 >= 0.5 else "keep"
            rel = relation(truth, new, etext)
            out.append({"run": "dev-3 B", "step": e["step"], "stage": int(new[1:].split(".")[0]), "new": new,
                        "new_kind": kinds[new], "entry": ent, "p_replace": p1, "p_modify": p2, "action": action,
                        "truth": rel, "class": classify(rel, action, int(new[1:].split(".")[0]) <= 2)})
    return out


def decisions_dev4() -> list[dict]:
    run, truth, ev, prim = load(B4)
    kinds = {i["id"]: i["kind"] for i in truth["items"]}
    text = {i["id"]: " ".join(i["text"].split()) for i in truth["items"]}
    out = []
    for p in prim:
        if p.get("status") != "ok" or not p["request"]["question"].startswith("Does the NEW change item modify"):
            continue
        new = next((n for n, t in text.items() if t[:60] in p["request"]["background"]), None)
        if new is None:
            continue
        rep = next((x for x in prim if x["step"] == p["step"] and x.get("status") == "ok"
                    and x["request"]["question"].startswith("Does the NEW change item completely")
                    and x["request"]["background"] == p["request"]["background"]), None)
        for it in p["request"]["items"]:
            pm = p["answers"].get(it["key"]) or 0
            pr = (rep["answers"].get(it["key"]) if rep else None) if pm > 0.5 else None
            action = "keep" if pm <= 0.5 else ("retire" if (pr or 0) > 0.75 else "amend")
            rel = relation(truth, new, it["text"])
            out.append({"run": "dev-4 B", "step": p["step"], "stage": int(new[1:].split(".")[0]), "new": new,
                        "new_kind": kinds[new], "entry": it["key"], "p_modify": pm, "p_replace": pr, "action": action,
                        "truth": rel, "class": classify(rel, action, False)})
    return out


def register_lines(run: Path, rev: int) -> list[str]:
    doc = json.loads((run / "context" / f"rev-{rev:04d}.json").read_text())
    out = []
    for e in doc["entries"]:
        if not RUNTIME_ID.match(e["id"]):
            out += [ln.strip() for ln in e["body"].splitlines() if ln.lstrip(" -*").startswith(("CURRENT", "HISTORY"))]
    return out


def growth(rid: str) -> list[dict]:
    run, truth, ev, _ = load(rid)
    reg = json.loads((run / "evaluator" / "register_score.json").read_text())
    texts = {" ".join(i["text"].split())[:50] for i in truth["items"]}
    rows = []
    for st in reg["stages"]:
        ls = register_lines(run, st["revision"])
        body = [re.sub(r"^(CURRENT|HISTORY)[^\]]*\]\s*", "", x) for x in ls]
        amend_lines = [x for x in ls if "amends the above" in x]
        dup = sum(1 for x in amend_lines if any(x.split("this wins: ", 1)[-1][:50] == y.split("] ", 1)[-1][:50]
                                                 for y in ls if y.startswith("CURRENT [") and "amends the above" not in y))
        rows.append({
            "stage": st["stage"], "lines": len(ls), "chars": sum(map(len, ls)),
            "current": sum(x.startswith("CURRENT") for x in ls), "history": sum(x.startswith("HISTORY") for x in ls),
            "verbatim_lines": sum(any(t[:40] in " ".join(b.split()) for t in texts) for b in body),
            "duplicated_amendments": dup,
            "footer_text": sum("Visible tests for the rules" in x for x in ls),
            "information_as_current": sum(x.startswith("CURRENT") and "For information" in x for x in ls),
        })
    return rows


def step_roles(rid: str) -> dict:
    """Main-model cost, output and cache writes by step role (from the step scripts)."""
    run, _, ev, _ = load(rid)
    resp = {e["step"]: e for e in ev if e["event"] == "response"}
    scripts = {e["step"]: (run / e["script"]).read_text() for e in ev if e["event"] == "execution_start"}
    released = {e["step"] for e in ev if e["event"] == "stage_released"}
    roles: dict[str, dict[str, float]] = {}
    for step, r in resp.items():
        code = scripts.get(step, "")
        if step in released:
            role = "advance"
        elif re.search(r"open\(['\"][^'\"]*(reghelper|regmaint)\.py['\"],\s*['\"]w", code):
            role = "helper setup" if step == min(scripts) + 1 or "def update" in code else "helper revision"
        elif re.search(r"\b(reghelper|regmaint)\.override\(", code):
            role = "override / correction"
        elif re.search(r"\.update\(\d+\)", code):
            role = "helper call (+ code change)"
        elif step not in scripts:
            role = "final / other"
        else:
            role = "code / inspection only" if "CURRENT [" not in code else "direct register edit (+ code)"
        d = roles.setdefault(role, {"steps": 0, "usd": 0.0, "output": 0, "cache_write": 0})
        u = r["usage"]
        d["steps"] += 1
        d["usd"] = round(d["usd"] + r["cost_usd"], 6)
        d["output"] += u["output_tokens"]
        d["cache_write"] += u.get("cache_creation_input_tokens", 0)
    return roles


def main() -> None:
    rows = decisions_dev3() + decisions_dev4()
    for run in ("dev-3 B", "dev-4 B"):
        rs = [r for r in rows if r["run"] == run]
        print(f"{run}: {len(rs)} pair decisions; classes: {dict(Counter(r['class'] for r in rs))}")
        for r in rs:
            if r["class"] not in ("correct keep",):
                print("   ", json.dumps(r))
    for rid, label in ((A3, "dev-3 A"), (B3, "dev-3 B"), (B4, "dev-4 B"), (A4, "dev-4 A")):
        print(label, "register growth:", json.dumps(growth(rid)))
        print(label, "step roles:", json.dumps(step_roles(rid)))


if __name__ == "__main__":
    main()
