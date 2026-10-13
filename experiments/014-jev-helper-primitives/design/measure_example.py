"""DEVELOPMENT MATERIAL for the proposed 014 comparison: size, selection-work and scoring checks on
the hand-written example instance (w3-example-instance.json). No clm-lib import, no API calls.

Usage (from this folder):  python measure_example.py

1. Replays the instance's truth to get, for every stage, what is in force, what was replaced,
   what is amended and which obligations are active.
2. Measures sizes against the runtime limits used by the W2 configs (8,000-token context
   budget; 3.0 characters per token, the runtime's initial estimate; a fixed prompt overhead of
   2,074 estimated tokens and up to ~1,900 tokens of step entries, both measured on the W2 runs).
3. Counts the selection work per notice and the jev-primitive/1 calls two plausible helper
   designs would need (limits: 20 items and 4,000 background characters per call, 4 calls per
   execution, 30 per run).
4. Prototypes the register scorer on four hand-made registers, to show the context state can be
   scored deterministically and independently of the agent's wording.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
INST = json.loads((HERE / "w3-example-instance.json").read_text())
ITEMS = {it["id"]: it for it in INST["items"]}
STAGES = max(it["stage"] for it in INST["items"])
CPT = 3.0  # characters per token: the runtime's initial estimate
FIXED_TOKENS = 2074  # system prompt + task text, measured on the W2 requests (est_input_tokens)
STEP_ENTRY_TOKENS = 1900  # largest runtime step entries seen in W2 requests (act/obs/rcpt), rounded up
BUDGET = 8000
REQUIREMENT_KINDS = {"rule", "exception", "obligation", "change"}


def state(stage: int) -> dict[str, dict]:
    """Truth after `stage`: per item, in force?, replaced by, amended by, activated."""
    st = {
        i: {"in_force": it["kind"] in REQUIREMENT_KINDS, "replaced_by": [], "amended_by": [], "active": it["kind"] != "obligation"}
        for i, it in ITEMS.items()
        if it["stage"] <= stage
    }
    for i, it in ITEMS.items():
        if it["stage"] > stage:
            continue
        for t in it.get("truth", []):
            s = st[t["target"]]
            if t["effect"] == "replaces":
                s["in_force"] = False
                s["replaced_by"].append(i)
            elif t["effect"] == "amends":
                s["amended_by"].append(i)
            elif t["effect"] == "activates":
                s["active"] = True
    return st


def measure() -> None:
    print("stage | items in force | replaced (history) | notice chars | verbatim register chars (est tokens) | est request tokens / budget")
    for s in range(1, STAGES + 1):
        st = state(s)
        in_force = [i for i, x in st.items() if x["in_force"]]
        hist = [i for i, x in st.items() if not x["in_force"] and ITEMS[i]["kind"] != "information"]
        notice = sum(len(ITEMS[i]["text"]) + 12 for i in ITEMS if ITEMS[i]["stage"] == s)
        reg = sum(len(ITEMS[i]["text"]) + 24 for i in in_force + hist)
        req = FIXED_TOKENS + STEP_ENTRY_TOKENS + math.ceil((reg + notice) / CPT)
        print(f"{s} | {len(in_force)} | {len(hist)} | {notice} | {reg} ({math.ceil(reg / CPT)}) | {req} / {BUDGET}")
    total_source = sum(len(it["text"]) + 12 for it in INST["items"])
    print(f"all source text verbatim: {total_source} chars ({math.ceil(total_source / CPT)} tokens)")

    print("\nnotice | entries before | items | pairs | truly affected entries (share) | 'none' distractor pairs | calls: per-entry design / per-pair design")
    for s in range(3, STAGES + 1):
        before = state(s - 1)
        entries = [i for i, x in before.items() if ITEMS[i]["kind"] != "information"]
        notice = [i for i in ITEMS if ITEMS[i]["stage"] == s]
        affected = {t["target"] for i in notice for t in ITEMS[i].get("truth", []) if t["effect"] != "none"}
        distract = sum(1 for i in notice for t in ITEMS[i].get("truth", []) if t["effect"] == "none")
        pairs = len(notice) * len(entries)
        bg = sum(len(ITEMS[i]["text"]) + 12 for i in notice)
        per_entry = math.ceil(len(entries) / 20) + math.ceil(len(affected) * len(notice) / 20)
        per_pair = math.ceil(pairs / 20)
        print(
            f"{s} | {len(entries)} | {len(notice)} | {pairs} | {len(affected)} ({len(affected) / len(entries):.0%}) | {distract} | "
            f"{per_entry} / {per_pair}{' (over 4 per execution)' if per_pair > 4 else ''}; background {bg} chars"
        )


# ------------------------------------------------------------------ register scorer prototype
CITE = re.compile(r"S\d+\.\d+")


def score(register: list[str], stage: int) -> dict[str, list[str]]:
    """Score a register (entry bodies starting CURRENT or HISTORY, citing item ids) against the
    truth after `stage`. Wording is not judged; content correctness is the hidden checks' job."""
    st = state(stage)
    cur = [set(CITE.findall(b)) for b in register if b.startswith("CURRENT")]
    his = [set(CITE.findall(b)) for b in register if b.startswith("HISTORY")]
    in_cur = set().union(*cur) if cur else set()
    in_his = set().union(*his) if his else set()
    out: dict[str, list[str]] = {k: [] for k in ("stale_replaced", "stale_unamended", "incorrect_retirement", "lost_active_obligation", "omitted", "history_lost")}
    for i, x in st.items():
        kind = ITEMS[i]["kind"]
        if kind == "information":
            continue
        if kind in ("history", "withdrawal"):
            if i not in in_cur | in_his:
                out["history_lost"].append(i)
            continue
        if x["in_force"]:
            if i not in in_cur:
                if kind == "obligation" and x["active"]:
                    out["lost_active_obligation"].append(i)  # filed as history or dropped
                elif i in in_his:
                    out["incorrect_retirement"].append(i)
                else:
                    out["omitted"].append(i)
            elif x["amended_by"] and not any(a in in_cur for a in x["amended_by"]):
                out["stale_unamended"].append(i)
        else:
            if any(i in e and not (e & set(x["replaced_by"])) for e in cur):
                out["stale_replaced"].append(i)
            if i not in in_his and not any(i in e and e & set(x["replaced_by"]) for e in cur):
                out["history_lost"].append(i)
    return {k: v for k, v in out.items() if v}


def example_registers() -> dict[str, list[str]]:
    """Four hand-made registers after stage 7 (bodies abbreviated)."""
    good = [
        "CURRENT [S3.1, S7.1] JSON records: id, title, owner, amount, project; ascending id",
        "CURRENT [S5.2] viewers export only their own records",
        "CURRENT [S1.3, S3.2] admins: any project; others: their projects plus records they own",
        "CURRENT [S1.4, S4.1] active only; archived only for admins with include_archived",
        "CURRENT [S1.5, S5.1] confidential: only admin with purpose audit or legal",
        "CURRENT [S1.6] amount exactly as given",
        "CURRENT [S2.1, S6.1] since: updated date if present, else created",
        "CURRENT [S2.3, S6.3] max_records, capped at 100",
        "CURRENT [S2.4, S6.2] exported_by = user name, except admin exports",
        "CURRENT [S2.5, S4.3] titles trimmed, internal whitespace collapsed",
        "CURRENT [S2.6] confidential_count when confidential exported for a non-audit purpose (now relevant: legal)",
        "HISTORY [S1.1] CSV format until stage 3; [S1.2] viewers raised PermissionError until stage 5",
        "HISTORY [S2.2, S4.2] EU residency rule, withdrawn at stage 7 [S7.2]",
        "HISTORY [S1.7] CSV chosen for finance spreadsheets; [S5.3] JSON chosen for the reporting API",
    ]
    marker_only = [b.replace("[S1.3, S3.2]", "[S1.3] (REVIEW)").replace("[S1.4, S4.1]", "[S1.4] (REVIEW)") for b in good]
    marker_only.append("CURRENT [S1.2] (REVIEW) viewers raise PermissionError")
    over_retire = [b for b in good if "S2.5" not in b] + ["HISTORY [S2.5] trimming (superseded by S4.3)", "CURRENT [S4.3] collapse internal whitespace"]
    fulfilled = [b for b in good if "S2.6" not in b] + ["HISTORY [S2.6] confidential_count obligation (fulfilled)"]
    return {"correct": good, "marker-only": marker_only, "over-retired partial change": over_retire, "obligation filed as done": fulfilled}


def main() -> None:
    measure()
    print("\nregister scorer prototype (after stage 7):")
    for name, reg in example_registers().items():
        print(f"- {name}: {score(reg, STAGES) or 'no errors'}")


if __name__ == "__main__":
    main()
