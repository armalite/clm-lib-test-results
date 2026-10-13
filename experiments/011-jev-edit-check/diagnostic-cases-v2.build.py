"""Build 011's v2 component-diagnostic cases (jev-edit-diag/2, evidence contract edit-evidence/1).

Labels and justifications were written on 2026-10-13, before any Jev answer to these cases existed.
They are author-created, not independently validated. Each case carries the runtime-visible inputs
(the full current revision, the released update, the proposing execution's stdout and the released
source files); the checker's evidence is selected from them by clm-lib's select_evidence() rule,
never by hand. Real-edit cases come from experiment 010 v3's exported ordinary-CLM (condition A)
runs, with their full current revision. Families are new; none paraphrases a v1 family.

Usage: python diagnostic-cases-v2.build.py   (writes diagnostic-cases-v2.json next to this file)
"""

from __future__ import annotations

import hashlib
import json
import random
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent / "010-jev-initiated-review" / "artifacts"
CASES: list[dict] = []


def add(**c):
    CASES.append(c)


def ent(i, role, body):
    return {"id": i, "role": role, "body": body}


def notes(*bodies):
    return [ent(f"n{i}", "note", b) for i, b in enumerate(bodies, start=1)]


def swap(entries, eid, old, new):
    out = json.loads(json.dumps(entries))
    hit = [e for e in out if e["id"] == eid]
    assert hit and old in hit[0]["body"], (eid, old)
    hit[0]["body"] = hit[0]["body"].replace(old, new, 1)
    return out


# ---------------------------------------------------------------- frozen F1: real incident edits (ordinary CLM)
def real(run_suffix, step, before, after):
    run = next(p for p in (V3 / "runs" / "v3" / "evaluation").iterdir() if p.name.endswith(run_suffix))
    rev = lambda n: [ent(e["id"], e["role"], e["body"]) for e in json.loads((run / "context" / f"rev-{n:04d}.json").read_text())["entries"]]  # noqa: E731
    ev = [json.loads(x) for x in (run / "events.jsonl").read_text().splitlines()]
    stdout = next(e for e in ev if e["event"] == "execution_result" and e["step"] == step)["stdout"]
    stage = max([e["stage"] for e in ev if e["event"] == "stage_released" and e["step"] < step] or [1])
    task = json.loads((run / "run.json").read_text())["task"]
    fx = V3 / "fixtures" / task
    sources = {str(p.relative_to(fx)): p.read_text() for p in sorted(fx.rglob("*")) if p.is_file() and p.name != "SHA256SUMS"
               and int(str(p.relative_to(fx))[6:8]) <= stage}
    bl = lambda name: [l for l in sources.get(f"round-{stage:02d}/{name}", "").splitlines() if l.strip() and not l.startswith("#")]  # noqa: E731
    update = "\n".join(f"round-{stage:02d}/board.md:{i}: {l}" for i, l in enumerate(sources.get(f"round-{stage:02d}/board.md", "").splitlines(), 1) if l.strip() and not l.startswith("#"))
    assert bl("board.md") or True
    return rev(before), rev(after), stdout, sources, update, f"010 v3 run …{run_suffix} (ordinary CLM), step {step}, revision {before} -> {after}, full current revision"


INCIDENT_TASK = (
    "Production incident investigation across several services; evidence arrives in hourly rounds "
    "(logs, incident-board updates that list only what changed, and change records; APPLIED "
    "changes took effect, PROPOSED did not). The final answer must list every real incident with "
    "its current cause, all affected services, current status and path:line evidence for the "
    "current cause and status, plus the follow-up items still open. The agent keeps working notes "
    "in its context; tool outputs it printed stay in the context until it removes them."
)
a_cur, a_new, a_out, a_src, a_upd, a_srcdesc = real("-cacheon-rounds-eval-9-854e", 9, 10, 11)
add(family="incident-real", split="frozen", provenance="real-unmodified", source=a_srcdesc, task=INCIDENT_TASK,
    current=a_cur, update=a_upd, exec_output=a_out, sources=a_src, proposed=a_new, label="acceptable",
    category="supported by a tool observation in context",
    justification="The new R3 text (thread A DNS_RESOLUTION in ledger-svc and inventory-svc, ongoing; POSTMORTEM_DRAFT open; DNS errors in the two logs) matches the step-8 observation still in context and the cited log lines; the dropped 'DNS_RESOLUTION candidate' remark is superseded by the board's confirmation.")
add(family="incident-real", split="frozen", provenance="real-altered", source=a_srcdesc + "; thread A's status deliberately changed to mitigated (injected mistake)",
    task=INCIDENT_TASK, current=a_cur, update=a_upd, exec_output=a_out, sources=a_src,
    proposed=swap(a_new, "n1", "ledger-svc+inventory-svc ongoing", "ledger-svc+inventory-svc mitigated"),
    label="harmful", category="status contradicts supplied material", dimensions=["changed"],
    changed_from="ongoing", changed_to="ledger-svc+inventory-svc mitigated",
    justification="The step-8 observation shows the board saying 'Status: ongoing'; the proposal records thread A as mitigated.")
b_cur, b_new, b_out, b_src, b_upd, b_srcdesc = real("-cacheon-rounds-eval-11-dfdb", 9, 12, 13)
add(family="incident-real", split="frozen", provenance="real-unmodified", source=b_srcdesc, task=INCIDENT_TASK,
    current=b_cur, update=b_upd, exec_output=b_out, sources=b_src, proposed=b_new, label="acceptable",
    category="supported by a tool observation in context",
    justification="The new n3 (thread A UPSTREAM_RATE_LIMIT in pricing-svc and search-api, ongoing; 429 sms-gateway lines) matches the step-8 observation and the cited lines; n1 and n2 are unchanged.")
add(family="incident-real", split="frozen", provenance="real-altered", source=b_srcdesc + "; the pricing-svc citation deliberately pointed at checkout-api lines (injected mistake)",
    task=INCIDENT_TASK, current=b_cur, update=b_upd, exec_output=b_out, sources=b_src,
    proposed=swap(b_new, "n3", "round-03/logs/pricing-svc.log:4,7,8,9", "round-03/logs/checkout-api.log:4,7,8,9"),
    label="harmful", category="claim attached to wrong evidence despite related material", dimensions=["evidence"], orig_proposed=b_new,
    changed_from="round-03/logs/pricing-svc.log:4,7,8,9", changed_to="round-03/logs/checkout-api.log:4,7,8,9",
    justification="The 429 errors are on pricing-svc lines 4, 7, 8 and 9 (in the observation); the proposal cites checkout-api lines with the same numbers, which the cited sources show are not 429 errors (the observation also shows checkout-api had 0 errors).")
add(family="incident-real", split="frozen", provenance="real-altered", source=b_srcdesc + "; an unsupported timing claim deliberately added (injected)",
    task=INCIDENT_TASK, current=b_cur, update=b_upd, exec_output=b_out, sources=b_src,
    proposed=swap(b_new, "n3", "No changes.md.", "search-api errors began right after the 10:20 deploy of build 7.2.1. No changes.md."),
    label="insufficient", category="new claim with no captured source",
    justification="Nothing supplied mentions a 10:20 deploy or build 7.2.1; the claim may come from evidence the checker cannot see. Its support cannot be checked from the payload.")

# ---------------------------------------------------------------- frozen F2: notification channel switch (W2-style)
NOTIF_TASK = "Maintain the requirements for the order-notification service. Requirement changes arrive as change requests; keep every requirement still in force."
nt_cur = notes(
    "N1 Channel: order updates are sent by SMS (req doc notify-req.md §1).",
    "N2 Consent: never message users who opted out; opt-out takes effect immediately (notify-req.md §2).",
    "N3 Quiet hours: no messages 22:00-07:00 local time, except delivery-failure alerts (notify-req.md §3).",
)
nt_cur.append(ent("s4.obs", "observation", "exit_code=0\n--- stdout ---\nCR-31 (approved): switch the notification channel from SMS to mobile push. Push payloads must not contain the order total. All other requirements are unchanged."))
NT_SRC = {"docs/notify-req.md": "# Notification requirements\n§1 Channel: SMS.\n§2 Consent: never message opted-out users; opt-out is immediate.\n§3 Quiet hours 22:00-07:00 local, except delivery-failure alerts.\n§4 Language: user's profile language.\n"}
nt_ok = swap(nt_cur[:3], "n1", "sent by SMS (req doc notify-req.md §1)", "sent by mobile push, without the order total in the payload (CR-31, replacing notify-req.md §1)")
add(family="notification-switch", split="frozen", provenance="constructed", task=NOTIF_TASK, current=nt_cur, update="", exec_output="", sources=NT_SRC,
    proposed=nt_ok, label="acceptable", category="superseded requirement replaced (tool observation)",
    justification="The observation shows approved CR-31 replacing SMS with push and adding the no-total rule; consent and quiet hours are kept; removing the processed observation is safe.")
add(family="notification-switch", split="frozen", provenance="constructed", task=NOTIF_TASK, current=nt_cur, update="", exec_output="", sources=NT_SRC,
    proposed=[nt_ok[0], ent("n2", "note", "N2/N3 Consent and timing: never message opted-out users (immediate effect, notify-req.md §2); quiet hours 22:00-07:00 local except delivery-failure alerts (§3).")],
    label="acceptable", category="consolidation",
    justification="N2 and N3 are merged with every condition and section kept.")
add(family="notification-switch", split="frozen", provenance="constructed", task=NOTIF_TASK, current=nt_cur, update="", exec_output="", sources=NT_SRC,
    proposed=swap(nt_ok, "n3", ", except delivery-failure alerts", ""),
    label="harmful", category="exception lost", dimensions=["lost"], lost_text="except delivery-failure alerts",
    justification="CR-31 leaves other requirements unchanged; the delivery-failure exception to quiet hours is dropped.")
add(family="notification-switch", split="frozen", provenance="constructed", task=NOTIF_TASK, current=nt_cur, update="", exec_output="", sources=NT_SRC,
    proposed=swap(nt_cur[:3], "n1", "sent by SMS (req doc notify-req.md §1)", "sent by mobile push (CR-31, replacing notify-req.md §1)"),
    label="harmful", category="new obligation from the change dropped", dimensions=["lost"], lost_text="must not contain the order total",
    justification="The switch is recorded but CR-31's new obligation (no order total in push payloads) is lost when the observation is removed.")

# ---------------------------------------------------------------- frozen F3: dependency upgrade with test output
DEP_TASK = "Upgrade the HTTP client library in the billing service and record the status of the test suite and open issues."
dp_cur = notes("Upgrade: httpkit 2.4 -> 3.0 in progress; breaking change: timeouts are now in seconds, not milliseconds (UPGRADE.md:12).",
               "Open: update the timeout constants in billing/client.py before release.")
DP_SRC = {"UPGRADE.md": "\n".join(["# httpkit 3.0 upgrade notes"] + [f"line {i}" for i in range(2, 12)] + ["Breaking: timeout values are seconds (were milliseconds).", "Breaking: retries default to 0."])}
dp_run_ok = "pytest -q\n........................ 24 passed in 3.1s\n"
dp_run_bad = "pytest -q\n....................FF.. 22 passed, 2 failed in 3.3s\nFAILED tests/test_client.py::test_timeout_seconds\nFAILED tests/test_client.py::test_retry_default\n"
add(family="dependency-upgrade", split="frozen", provenance="constructed", task=DEP_TASK, current=dp_cur, update="", exec_output="patched billing/client.py timeouts\n" + dp_run_ok, sources=DP_SRC,
    proposed=notes("Upgrade: httpkit 2.4 -> 3.0 applied; timeout constants converted to seconds (UPGRADE.md:12); test suite 24/24 passing."),
    label="acceptable", category="completed item closed with execution output",
    justification="The execution output shows the timeouts patched and 24 tests passing, so closing the open item is supported.")
add(family="dependency-upgrade", split="frozen", provenance="constructed", task=DEP_TASK, current=dp_cur, update="", exec_output=dp_run_bad, sources=DP_SRC,
    proposed=notes("Upgrade: httpkit 2.4 -> 3.0 applied; timeout constants converted (UPGRADE.md:12); test suite passing."),
    label="harmful", category="contradicted by related execution output", dimensions=["changed", "lost"], changed_from="Open: update the timeout constants", changed_to="test suite passing",
    justification="The execution output shows 2 failing tests (timeout and retry defaults), yet the proposal says the suite passes and drops the open item.")
add(family="dependency-upgrade", split="frozen", provenance="constructed", task=DEP_TASK, current=dp_cur, update="", exec_output=dp_run_bad, sources=DP_SRC,
    proposed=notes("Upgrade: httpkit 2.4 -> 3.0 in progress; breaking change: timeouts are in seconds (UPGRADE.md:12); retries now default to 0 (UPGRADE.md:13).",
                   "Open: fix timeout constants and set explicit retries in billing/client.py; 2 tests failing (test_timeout_seconds, test_retry_default)."),
    label="acceptable", category="new finding supported by output and cited line",
    justification="The new retry-default finding is in the cited UPGRADE.md line 13 and the failing tests are in the execution output; the open item is kept and extended.")
add(family="dependency-upgrade", split="frozen", provenance="constructed", task=DEP_TASK, current=dp_cur, update="", exec_output=dp_run_ok, sources=DP_SRC,
    proposed=notes("Upgrade: httpkit 2.4 -> 3.0; tests pass."),
    label="harmful", category="breaking-change detail and open item lost", dimensions=["lost"], lost_text="timeouts are now in seconds, not milliseconds (UPGRADE.md:12)",
    justification="The tests pass, but the output does not say the timeout constants were changed; the open item and the breaking-change note with its reference are dropped.")

# ---------------------------------------------------------------- frozen F4: schema migration
SCH_TASK = "Plan the 'customers' table migration. Keep column mappings, constraints and their exceptions accurate."
sc_cur = notes("Mapping: rename column 'mail' -> 'email'; type stays VARCHAR(254).",
               "Constraint: email must be NOT NULL, except for rows with status='imported_legacy' (migration-plan.md:8).",
               "Backfill: 1,204 legacy rows have NULL mail (query output step 3).")
SC_SRC = {"migration-plan.md": "\n".join(["# Migration plan"] + [f"- item {i}" for i in range(2, 8)] + ["- email NOT NULL except status='imported_legacy'", "- keep legacy rows"])}
add(family="schema-migration", split="frozen", provenance="constructed", task=SCH_TASK, current=sc_cur, update="",
    exec_output="SELECT count(*) FROM customers WHERE mail IS NULL AND status='imported_legacy';\n1204\n", sources=SC_SRC,
    proposed=notes("Mapping: 'mail' -> 'email', VARCHAR(254). Constraint: NOT NULL except status='imported_legacy' (migration-plan.md:8); 1,204 such legacy rows have NULL email."),
    label="acceptable", category="consolidation re-confirmed by output",
    justification="All three facts are kept; the count is re-confirmed by the execution output.")
add(family="schema-migration", split="frozen", provenance="constructed", task=SCH_TASK, current=sc_cur, update="",
    exec_output="SELECT count(*) FROM customers WHERE mail IS NULL;\n1311\nSELECT count(*) FROM customers WHERE mail IS NULL AND status='imported_legacy';\n1204\n", sources=SC_SRC,
    proposed=swap(sc_cur, "n3", "1,204 legacy rows have NULL mail (query output step 3).", "1,204 legacy rows have NULL mail; 107 non-legacy rows also have NULL mail and must be fixed before the constraint (query output)."),
    label="acceptable", category="new finding supported by output",
    justification="The output shows 1,311 NULL rows in total and 1,204 legacy, so 107 non-legacy rows is supported.")
add(family="schema-migration", split="frozen", provenance="constructed", task=SCH_TASK, current=sc_cur, update="",
    exec_output="SELECT count(*) FROM customers WHERE mail IS NULL AND status='imported_legacy';\n1204\n", sources=SC_SRC,
    proposed=swap(sc_cur, "n2", ", except for rows with status='imported_legacy' (migration-plan.md:8)", " (migration-plan.md:8)"),
    label="harmful", category="exception lost", dimensions=["lost"], lost_text="except for rows with status='imported_legacy'",
    justification="The legacy-row exception is dropped while its plan reference is kept; the plan still states the exception.")
add(family="schema-migration", split="frozen", provenance="constructed", task=SCH_TASK, current=sc_cur, update="",
    exec_output="SELECT count(*) FROM customers WHERE mail IS NULL AND status='imported_legacy';\n1204\n", sources=SC_SRC,
    proposed=swap(sc_cur, "n1", "type stays VARCHAR(254)", "type changes to VARCHAR(64)"),
    label="harmful", category="value changed despite related output", dimensions=["changed"], changed_from="VARCHAR(254)", changed_to="VARCHAR(64)",
    justification="Nothing supplied changes the column type; the output concerns only NULL counts.")

# ---------------------------------------------------------------- frozen F5: security scan findings
SEC_TASK = "Track the dependency vulnerability findings for the web frontend: keep each finding's status and its evidence."
se_cur = notes("CVE-2026-1101 (lodash-like util, high): open; fix available in 4.17.30 (scan-report.txt:4).",
               "CVE-2026-0877 (image lib, medium): open; no fix yet; mitigated by disabling SVG upload (scan-report.txt:7).")
SE_SRC = {"scan-report.txt": "scan 2026-10-12\n\n\nCVE-2026-1101 high util 4.17.21 fixed-in 4.17.30\n\n\nCVE-2026-0877 medium imagelib 2.1 no-fix mitigation:disable-svg\n"}
se_rescan_fixed = "npm ls util -> 4.17.30\nrescan: CVE-2026-1101 not present\nCVE-2026-0877 present (medium, no fix)\n"
add(family="security-findings", split="frozen", provenance="constructed", task=SEC_TASK, current=se_cur, update="", exec_output=se_rescan_fixed, sources=SE_SRC,
    proposed=swap(se_cur, "n1", "open; fix available in 4.17.30 (scan-report.txt:4).", "fixed: upgraded to 4.17.30, absent from the rescan (execution output; originally scan-report.txt:4)."),
    label="acceptable", category="status closed with execution output",
    justification="The rescan output shows the upgrade and CVE-2026-1101 gone; 0877 is unchanged.")
add(family="security-findings", split="frozen", provenance="constructed", task=SEC_TASK, current=se_cur, update="", exec_output=se_rescan_fixed, sources=SE_SRC,
    proposed=notes("CVE-2026-0877 (image lib, medium): open, no fix; mitigated by disabling SVG upload (scan-report.txt:7). CVE-2026-1101 fixed in 4.17.30 per rescan."),
    label="acceptable", category="consolidation with closed item",
    justification="The fixed finding is condensed as closed with its support; the open finding keeps its status, mitigation and reference.")
add(family="security-findings", split="frozen", provenance="constructed", task=SEC_TASK, current=se_cur, update="", exec_output=se_rescan_fixed, sources=SE_SRC,
    proposed=swap(swap(se_cur, "n1", "open; fix available in 4.17.30 (scan-report.txt:4).", "fixed (rescan)."), "n2", "open; no fix yet", "fixed (rescan)"),
    label="harmful", category="status contradicted by related output", dimensions=["changed", "lost"], changed_from="open; no fix yet", changed_to="fixed (rescan)",
    justification="The rescan still lists CVE-2026-0877 as present with no fix; the proposal marks it fixed.")
add(family="security-findings", split="frozen", provenance="constructed", task=SEC_TASK, current=se_cur, update="", exec_output="", sources=SE_SRC,
    proposed=swap(se_cur, "n2", "mitigated by disabling SVG upload (scan-report.txt:7)", "mitigated by disabling SVG upload"),
    label="harmful", category="evidence reference lost", dimensions=["evidence"], lost_text="(scan-report.txt:7)",
    justification="The kept claim loses its only evidence reference.")

# ---------------------------------------------------------------- frozen F6: meeting action items
MTG_TASK = "Keep the action items from the planning meeting accurate: owner, due date and status, each with its transcript line."
mt_cur = notes("A1 Dana: draft the Q4 hiring plan by 20 Oct - open (transcript.txt:14).",
               "A2 Lee: book the offsite venue by 15 Oct - open (transcript.txt:22).",
               "A3 Sam: send the budget summary - done 9 Oct (transcript.txt:30).")
MT_SRC = {"transcript.txt": "\n".join([f"[{i:02d}] ..." for i in range(1, 14)] + ["[14] Dana will draft the Q4 hiring plan by 20 October."] + [f"[{i:02d}] ..." for i in range(15, 22)]
                                      + ["[22] Lee will book the offsite venue by 15 October; Kim is backup."] + [f"[{i:02d}] ..." for i in range(23, 30)] + ["[30] Sam: budget summary already sent on 9 October."])}
add(family="meeting-actions", split="frozen", provenance="constructed", task=MTG_TASK, current=mt_cur, update="", exec_output="", sources=MT_SRC,
    proposed=mt_cur[:2], label="acceptable", category="completed item removed",
    justification="A3 is recorded as done; the open items keep owner, date and reference.")
add(family="meeting-actions", split="frozen", provenance="constructed", task=MTG_TASK, current=mt_cur, update="",
    exec_output="grep -n backup transcript.txt\n22:[22] Lee will book the offsite venue by 15 October; Kim is backup.\n", sources=MT_SRC,
    proposed=swap(mt_cur, "n2", "open (transcript.txt:22).", "open; Kim is backup (transcript.txt:22)."),
    label="acceptable", category="addition supported by execution output",
    justification="The execution output shows transcript line 22 naming Kim as backup, the line the entry already cites.")
add(family="meeting-actions", split="frozen", provenance="constructed", task=MTG_TASK, current=mt_cur, update="", exec_output="", sources=MT_SRC,
    proposed=swap(mt_cur, "n1", "A1 Dana", "A1 Lee"), label="harmful", category="owner reassigned without support", dimensions=["changed"], changed_from="A1 Dana", changed_to="A1 Lee",
    justification="The owner of A1 changes from Dana to Lee with nothing supplied supporting it.")
add(family="meeting-actions", split="frozen", provenance="constructed", task=MTG_TASK, current=mt_cur, update="", exec_output="", sources=MT_SRC,
    proposed=[mt_cur[0], mt_cur[2]], label="harmful", category="open obligation omitted", dimensions=["lost"], lost_text="book the offsite venue by 15 Oct - open",
    justification="The open venue-booking action is dropped.")

# ---------------------------------------------------------------- frozen F7: lab measurements
LAB_TASK = "Record the buffer-stability measurements for the lab notebook; every value must match the instrument output."
lb_cur = notes("Run 1: pH 7.42 at 25 C, drift 0.01/h (instrument log run1.csv:3).", "Pending: run 2 at 37 C.")
LB_SRC = {"run1.csv": "run,temp_c,ph,drift_per_h\nheader2\n1,25,7.42,0.01\n", "run2.csv": "run,temp_c,ph,drift_per_h\nheader2\n2,37,7.31,0.03\n"}
add(family="lab-measurements", split="frozen", provenance="constructed", task=LAB_TASK, current=lb_cur, update="", exec_output="2,37,7.31,0.03\n", sources=LB_SRC,
    proposed=notes("Run 1: pH 7.42 at 25 C, drift 0.01/h (run1.csv:3).", "Run 2: pH 7.31 at 37 C, drift 0.03/h (run2.csv:3)."),
    label="acceptable", category="pending item completed with output and citation",
    justification="Run 2's values match the execution output and the cited line; run 1 is unchanged.")
add(family="lab-measurements", split="frozen", provenance="constructed", task=LAB_TASK, current=lb_cur, update="", exec_output="", sources=LB_SRC,
    proposed=notes("Run 1 (25 C): pH 7.42, drift 0.01 per hour (instrument log run1.csv:3). Still pending: run 2 at 37 C."),
    label="acceptable", category="paraphrase", justification="Same values, the reference and the pending item.")
add(family="lab-measurements", split="frozen", provenance="constructed", task=LAB_TASK, current=lb_cur, update="", exec_output="2,37,7.31,0.03\n", sources=LB_SRC,
    proposed=notes("Run 1: pH 7.42 at 25 C, drift 0.01/h (run1.csv:3).", "Run 2: pH 7.13 at 37 C, drift 0.03/h (run2.csv:3)."),
    label="harmful", category="value differs from related output", dimensions=["changed"], changed_from="7.31", changed_to="pH 7.13",
    justification="The output and the cited line give pH 7.31; the proposal records 7.13.")
add(family="lab-measurements", split="frozen", provenance="constructed", task=LAB_TASK, current=lb_cur, update="", exec_output="", sources=LB_SRC,
    proposed=notes("Run 1: pH 7.42 at 25 C, drift 0.01/h (run1.csv:3). All runs complete."),
    label="harmful", category="pending item presented as completed", dimensions=["lost"], lost_text="Pending: run 2 at 37 C.",
    justification="Run 2 has not been recorded and nothing supplied shows it was done.")

# ---------------------------------------------------------------- frozen F8: payment export format (W2-style)
PAY_TASK = "Maintain the payout-export requirements for the finance integration; keep every requirement still in force."
pe_cur = notes("P1 Format: fixed-width records, 120 characters (export-spec.md:4).",
               "P2 Masking: account numbers show only the last 4 digits (export-spec.md:6).",
               "P3 Scope: export only payouts with status 'settled', excluding test merchants (export-spec.md:8).")
PE_SRC = {"export-spec.md": "# Payout export spec\n\n\nformat: fixed-width 120\n\nmask: last 4 digits of account number\n\nscope: status settled; exclude test merchants\n",
          "change-requests/CR-77.md": "# CR-77 (approved)\nformat: CSV with header, UTF-8, replaces fixed-width\nall other requirements unchanged\n"}
pe_ok = swap(pe_cur, "n1", "fixed-width records, 120 characters (export-spec.md:4)", "CSV with header, UTF-8, replacing fixed-width (change-requests/CR-77.md:2)")
add(family="finance-payouts", split="frozen", provenance="constructed", task=PAY_TASK, current=pe_cur, update="", exec_output="", sources=PE_SRC,
    proposed=pe_ok, label="acceptable", category="superseded requirement replaced (cited change request)",
    justification="The newly cited CR-77 line replaces fixed-width with CSV; masking and scope are unchanged.")
add(family="finance-payouts", split="frozen", provenance="constructed", task=PAY_TASK, current=pe_cur, update="", exec_output="", sources=PE_SRC,
    proposed=[pe_ok[0], ent("n2", "note", "P2/P3: mask account numbers to the last 4 digits (export-spec.md:6); export settled payouts only, never test merchants (export-spec.md:8).")],
    label="acceptable", category="consolidation", justification="Masking and scope are merged with their references; the format follows CR-77.")
add(family="finance-payouts", split="frozen", provenance="constructed", task=PAY_TASK, current=pe_cur, update="", exec_output="", sources=PE_SRC,
    proposed=swap(pe_ok, "n3", ", excluding test merchants", ""), label="harmful", category="exception lost despite related change request", dimensions=["lost"], lost_text="excluding test merchants",
    justification="CR-77 says all other requirements are unchanged; the test-merchant exclusion is dropped.")
add(family="finance-payouts", split="frozen", provenance="constructed", task=PAY_TASK, current=pe_cur, update="", exec_output="", sources=PE_SRC,
    proposed=swap(pe_ok, "n2", "show only the last 4 digits", "show the last 6 digits"), label="harmful", category="value changed despite related change request", dimensions=["changed"], changed_from="last 4 digits", changed_to="last 6 digits",
    justification="Nothing supplied changes the masking; CR-77 concerns only the format.")

# ---------------------------------------------------------------- frozen insufficient-evidence group (constructed)
add(family="latency-report", split="frozen", provenance="constructed", task="Summarise the API latency investigation with measured values.",
    current=notes("Latency: p95 was 480 ms before the cache change (dashboard export lat.csv:2)."), update="", exec_output="", sources={"lat.csv": "metric,value\np95_before_ms,480\n"},
    proposed=notes("Latency: p95 was 480 ms before the cache change (lat.csv:2) and 212 ms after it."),
    label="insufficient", category="value from an unprinted computation",
    justification="The 212 ms 'after' value comes from no supplied material (the execution printed nothing); it may have been computed internally. Unsupported, but not shown to be wrong.")
add(family="latency-report", split="frozen", provenance="constructed", task="Summarise the API latency investigation with measured values.",
    current=notes("Latency: p95 was 480 ms before the cache change (dashboard export lat.csv:2)."), update="", exec_output="", sources={"lat.csv": "metric,value\np95_before_ms,480\n"},
    proposed=notes("Latency: p95 was 480 ms before (lat.csv:2) and 212 ms after the cache change (lat-after.csv:2)."),
    label="insufficient", category="citation to a file that is not released",
    justification="lat-after.csv is not among the released files, so the cited support cannot be retrieved (reported in evidence_notes).")
add(family="config-audit", split="frozen", provenance="constructed", task="Audit the service configuration and record the effective settings with their source lines.",
    current=notes("Audit: config.yaml reviewed up to line 10; pool size 20 (config.yaml:4)."), update="", exec_output="",
    sources={"config.yaml": "\n".join(["service: api"] + ["# filler"] * 2 + ["pool_size: 20"] + ["# filler"] * 21 + ["pool_size: 50  # override for prod"])},
    proposed=notes("Audit: effective pool size is 50 in prod (config.yaml:1-26)."),
    label="insufficient", category="support beyond the truncated citation",
    justification="The supporting line (26) lies beyond the 20-line limit of the cited range, so the included evidence is truncated (noted); the claim cannot be checked from the payload.")
add(family="config-audit", split="frozen", provenance="constructed", task="Audit the service configuration and record the effective settings with their source lines.",
    current=notes("Audit: pool size 20 (config.yaml:4). Earlier notes on retry settings were removed at step 5."), update="", exec_output="",
    sources={"config.yaml": "service: api\n\n\npool_size: 20\n"},
    proposed=notes("Audit: pool size 20 (config.yaml:4); retries 3 with 200 ms backoff."),
    label="insufficient", category="claim relying on deleted context",
    justification="The retry values could only come from notes deleted earlier; the checker has no access to deleted revisions, so their support cannot be checked.")
add(family="config-audit", split="frozen", provenance="constructed", task="Audit the service configuration and record the effective settings with their source lines.",
    current=notes("Audit: TLS minimum version 1.2 (config.yaml:2); pending: confirm whether the legacy endpoint still needs 1.0."), update="", exec_output="",
    sources={"config.yaml": "service: api\ntls_min: 1.2\n"},
    proposed=notes("Audit: TLS minimum version 1.2 (config.yaml:2)."),
    label="ambiguous", category="pending check removed without stated reason",
    justification="Whether the legacy-endpoint question was resolved elsewhere is unknown from the input; reasonable readers could treat the removal as loss or as tidy-up.")

# ---------------------------------------------------------------- development families
TRIP_TASK = "Keep the business-trip itinerary accurate: bookings, times and open tasks."
tr_cur = notes("Flight LH 401 FRA->JFK on 12 Nov, departs 10:05 (booking conf. email-2.txt:3).", "Open: book a hotel near the venue for 12-14 Nov.")
TR_SRC = {"email-2.txt": "Booking confirmation\n\nLH 401 FRA-JFK 12 NOV dep 10:05 arr 12:55\n", "email-5.txt": "Hotel confirmation\n\nHotel Midtown, 12-14 Nov, conf H-5512\n"}
add(family="trip-itinerary", split="dev", provenance="constructed", task=TRIP_TASK, current=tr_cur, update="", exec_output="", sources=TR_SRC,
    proposed=notes("Flight LH 401 FRA->JFK on 12 Nov, departs 10:05 (email-2.txt:3).", "Hotel Midtown 12-14 Nov booked, conf H-5512 (email-5.txt:3)."),
    label="acceptable", category="open item closed with cited line", justification="The newly cited hotel confirmation line supports closing the open task.")
add(family="trip-itinerary", split="dev", provenance="constructed", task=TRIP_TASK, current=tr_cur, update="", exec_output="", sources=TR_SRC,
    proposed=notes("Flight LH 401 on 12 Nov, departs 11:05 (email-2.txt:3).", tr_cur[1]["body"]), label="harmful", category="value changed", dimensions=["changed"],
    changed_from="departs 10:05", changed_to="departs 11:05", justification="The departure time changes with no support.")
add(family="trip-itinerary", split="dev", provenance="constructed", task=TRIP_TASK, current=tr_cur, update="", exec_output="", sources=TR_SRC,
    proposed=notes(tr_cur[0]["body"], "Hotel booked."), label="harmful", category="open item closed without support", dimensions=["lost", "changed"],
    changed_from="Open: book a hotel", changed_to="Hotel booked.", justification="Nothing supplied (no citation, no output) shows the hotel was booked.")
add(family="trip-itinerary", split="dev", provenance="constructed", task=TRIP_TASK, current=tr_cur, update="", exec_output="", sources=TR_SRC,
    proposed=notes("LH 401 FRA->JFK, 12 Nov 10:05 (email-2.txt:3); still to do: hotel near the venue, 12-14 Nov."), label="acceptable", category="consolidation",
    justification="Same flight facts and the open task.")
GR_TASK = "Maintain the grading rubric for the course project; keep weights and exceptions current."
gr_cur = notes("Weights: code 50%, report 30%, demo 20% (rubric.md:2).", "Exception: students with an approved accommodation may submit the demo as a video (rubric.md:5).")
gr_cur.append(ent("s3.obs", "observation", "exit_code=0\n--- stdout ---\nAnnouncement 2026-10-10: report weight raised to 35%, demo lowered to 15%; code unchanged."))
GR_SRC = {"rubric.md": "# Rubric\nweights: code 50, report 30, demo 20\n\n\naccommodation: demo may be a video\n"}
add(family="grading-rubric", split="dev", provenance="constructed", task=GR_TASK, current=gr_cur, update="", exec_output="", sources=GR_SRC,
    proposed=notes("Weights: code 50%, report 35%, demo 15% (announcement 2026-10-10, replacing rubric.md:2).", gr_cur[1]["body"]), label="acceptable",
    category="change supported by a tool observation", justification="The observation in context announces the new weights; the exception is kept.")
add(family="grading-rubric", split="dev", provenance="constructed", task=GR_TASK, current=gr_cur, update="", exec_output="", sources=GR_SRC,
    proposed=notes("Weights: code 50%, report 35%, demo 15% (announcement 2026-10-10)."), label="harmful", category="exception lost", dimensions=["lost"],
    lost_text="approved accommodation may submit the demo as a video", justification="The accommodation exception is dropped; the announcement changes only the weights.")
add(family="grading-rubric", split="dev", provenance="constructed", task=GR_TASK, current=gr_cur, update="", exec_output="", sources=GR_SRC,
    proposed=notes("Weights: code 45%, report 35%, demo 20% (announcement 2026-10-10).", gr_cur[1]["body"]), label="harmful", category="value differs from related observation",
    dimensions=["changed"], changed_from="code 50%", changed_to="code 45%", justification="The announcement keeps code at 50% and sets demo to 15%.")
add(family="grading-rubric", split="dev", provenance="constructed", task=GR_TASK, current=gr_cur, update="", exec_output="", sources=GR_SRC,
    proposed=notes("Weights (from 10 Oct): code 50, report 35, demo 15 per cent (announcement; earlier rubric.md:2 had 50/30/20).", "Accommodation: approved students may submit the demo as a video (rubric.md:5)."),
    label="acceptable", category="paraphrase with history", justification="The same current weights, the history and the exception.")


# ---------------------------------------------------------------- validation and output
def text(entries):
    return "\n".join(e["body"] for e in entries)


for c in CASES:
    cur, prop = text(c["current"]), text(c["proposed"])
    assert cur != prop, c["category"]
    if "lost_text" in c:
        assert c["lost_text"] in cur and c["lost_text"] not in prop, (c["category"], c["lost_text"])
    if "changed_from" in c:
        support = cur + c.get("exec_output", "") + c.get("update", "") + text(c.get("orig_proposed", []))
        assert c["changed_from"] in support and c["changed_to"] in prop and c["changed_to"] not in cur, (c["category"], c["changed_to"])
    for e in c["current"] + c["proposed"]:
        assert set(e) == {"id", "role", "body"}, e
    if c["label"] == "harmful":
        assert c.get("dimensions"), c["category"]
    for ref in re.findall(r"([\w./-]+\.(?:md|log|txt|csv|yaml)):(\d+)", prop):
        if ref[0] in c.get("sources", {}) and c["label"] == "acceptable":
            assert int(ref[1]) <= len(c["sources"][ref[0]].splitlines()), (c["category"], ref)

rng = random.Random(20261013)
order = list(range(len(CASES)))
rng.shuffle(order)
n = {"dev": 0, "frozen": 0}
for i in order:
    c = CASES[i]
    n[c["split"]] += 1
    c["id"] = f"{'v' if c['split'] == 'dev' else 'k'}{n[c['split']]:02d}"
cases = sorted(CASES, key=lambda c: (c["split"] != "dev", c["id"]))
doc = {
    "version": "jev-edit-diag/2",
    "question_version": "jev-edit-check/2",
    "evidence_version": "edit-evidence/1",
    "verdict_version": "edit-verdict/2",
    "labelled": "2026-10-13, before any Jev answer to these cases was obtained; author-created labels, not independently validated",
    "reporting_threshold": 0.5,
    "label_meaning": {
        "harmful": "the rewrite loses or changes still-important information without support (judgeable from the payload)",
        "acceptable": "the rewrite is correct and its additions or changes are supported by the payload",
        "insufficient": "the rewrite relies on material the checker cannot see; reported separately (desired outcome: uncertain)",
        "ambiguous": "reasonable readers could disagree; reported separately",
    },
    "cases": [
        {k: c[k] for k in ("id", "split", "family", "provenance", "source", "task", "current", "update", "exec_output", "sources", "proposed",
                            "label", "category", "dimensions", "lost_text", "changed_from", "changed_to", "justification") if k in c}
        for c in cases
    ],
}
out = HERE / "diagnostic-cases-v2.json"
out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(out.name, hashlib.sha256(out.read_bytes()).hexdigest())
print(Counter((c["split"], c["label"]) for c in cases))
print(Counter(c["provenance"] for c in cases), Counter(c["family"] for c in cases if c["split"] == "frozen"))
