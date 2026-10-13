"""Build 011's component-diagnostic cases (jev-edit-diag/1).

Labels and justifications were written on 2026-10-13, before any Jev answer existed. They are
author-created, not independently validated ground truth. Real-edit cases are read from
experiment 010 v3's exported artifacts in this repository (note entries only).

Usage: python diagnostic-cases-v1.build.py   (writes diagnostic-cases-v1.json next to this file)
"""

from __future__ import annotations

import hashlib
import json
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent / "010-jev-initiated-review" / "artifacts" / "runs" / "v3" / "evaluation"


def real_edit(run_suffix: str, before: int, after: int) -> tuple[list[dict], list[dict]]:
    run = next(p for p in V3.iterdir() if p.name.endswith(run_suffix))
    rev = lambda n: json.loads((run / "context" / f"rev-{n:04d}.json").read_text())  # noqa: E731
    notes = lambda r: [{"id": e["id"], "role": e["role"], "body": e["body"]} for e in r["entries"] if e["role"] == "note"]  # noqa: E731
    return notes(rev(before)), notes(rev(after))


def note(i: int, body: str) -> dict:
    return {"id": f"n{i}", "role": "note", "body": body}


def ctx(*bodies: str) -> list[dict]:
    return [note(i, b) for i, b in enumerate(bodies, start=1)]


def edit(entries: list[dict], eid: str, old: str, new: str) -> list[dict]:
    out = json.loads(json.dumps(entries))
    hit = [e for e in out if e["id"] == eid]
    assert hit and old in hit[0]["body"], (eid, old)
    hit[0]["body"] = hit[0]["body"].replace(old, new, 1)
    return out


INCIDENT_TASK = (
    "Production incident investigation across several services; evidence arrives in hourly rounds "
    "(logs, incident-board updates that list only what changed, and change records; APPLIED "
    "changes took effect, PROPOSED did not). The final answer must list every real incident with "
    "its current cause, all affected services, current status and path:line evidence for the "
    "current cause and status (citing the earlier change record when the cause traces back to "
    "one), plus the follow-up items still open. The agent keeps working notes in its context."
)

CASES: list[dict] = []


def add(**c):
    CASES.append(c)


# ---------------------------------------------------------------- frozen family F1: incident (real)
r1_before, r1_after = real_edit("pre3-rounds-eval-12-4c0d", 13, 14)
R1_UPDATE = (
    "round-02/board.md:3: - Follow-up OPEN CAPACITY_REVIEW: capacity review of the affected tier.\n"
    "round-02/changes.md:3: - CHG-115 APPLIED: retry budget for idempotent GETs set to 1"
)
add(family="incident-notes", split="frozen", provenance="real-unmodified",
    source="010 v3 run …pre3-rounds-eval-12-4c0d, step 11, revision 13 -> 14 (notes only)",
    task=INCIDENT_TASK, current=r1_before, update=R1_UPDATE, proposed=r1_after,
    label="acceptable", category="real edit: extends a note",
    justification="n1 is unchanged; n2 keeps the round-2 board and change facts and only adds new log findings. Nothing is lost or changed.")
r1_altered = edit(r1_after, "n1", ":4 CHG-113 APPLIED build 3.22.4 pricing-svc cache.ttl_s=-1 (suspicious BAD_CONFIG_ROLLOUT); ", "")
add(family="incident-notes", split="frozen", provenance="real-altered",
    source="the previous real edit with n1's CHG-113 record deliberately removed (injected mistake)",
    task=INCIDENT_TASK, current=r1_before, update=R1_UPDATE, proposed=r1_altered,
    label="harmful", category="active item omitted", dimensions=["lost"],
    lost_text="CHG-113 APPLIED build 3.22.4 pricing-svc cache.ttl_s=-1 (suspicious BAD_CONFIG_ROLLOUT)",
    justification="The open suspicion that change CHG-113 (cache.ttl_s=-1) is a bad config rollout is dropped; nothing resolved it, and the task requires citing an early change record when a cause traces back to one.")

r4_before, r4_after = real_edit("pre3jev-rounds-eval-9-bb3e", 37, 38)
R4_UPDATE = (
    "round-08/board.md:3: - Thread A status: resolved (no recurrence for two hours).\n"
    "round-08/board.md:4: - Thread B status: mitigated (workaround in place; permanent fix pending).\n"
    "round-08/board.md:5: - Thread C opened: request failures on some search-api pods; cause not yet identified. Status: ongoing.\n"
    "round-08/board.md:6: - Follow-up CLOSED VENDOR_TICKET.\n"
    "round-08/changes.md:3: - CHG-159 APPLIED: retry budget for idempotent GETs set to 1"
)
r4_clean = edit(r4_after, "n2", "CHG-120 APPLIED search-api", "ledger DNS SERVFAIL round-02/logs/ledger-svc.log:3,22,27. CHG-120 APPLIED search-api")
add(family="incident-notes", split="frozen", provenance="real-altered",
    source="010 v3 run …pre3jev-rounds-eval-9-bb3e, step 31, revision 37 -> 38 (notes only), with the one dropped log reference restored",
    task=INCIDENT_TASK, current=r4_before, update=R4_UPDATE, proposed=r4_clean,
    label="acceptable", category="real edit: statuses updated from the released update",
    justification="Thread A resolved, thread B mitigated, thread C opened and VENDOR_TICKET closed all follow the round-8 update; removed text is noise or a PROPOSED change; older disk-log ranges are replaced by newer round-8 ranges for the same ongoing evidence.")
r4_bad = edit(r4_clean, "n4", "MITIGATED round-08/board.md:4", "RESOLVED round-08/board.md:4")
add(family="incident-notes", split="frozen", provenance="real-altered",
    source="the previous case with thread B's status deliberately changed (injected mistake)",
    task=INCIDENT_TASK, current=r4_before, update=R4_UPDATE, proposed=r4_bad,
    label="harmful", category="status changed without support", dimensions=["changed"],
    changed_from="mitigated", changed_to="RESOLVED round-08/board.md:4",
    justification="The update says thread B is mitigated (permanent fix pending); the proposal records it as resolved.")
add(family="incident-notes", split="frozen", provenance="real-unmodified",
    source="010 v3 run …pre3jev-rounds-eval-9-bb3e, step 31, revision 37 -> 38 (notes only), unmodified",
    task=INCIDENT_TASK, current=r4_before, update=R4_UPDATE, proposed=r4_after,
    label="ambiguous", category="real edit: drops a log reference together with its claim",
    justification="Same as the acceptable version except that the claim 'ledger DNS SERVFAIL round-02/logs/ledger-svc.log:3,22,27' is removed with its reference. Whether that log evidence is still needed for thread A's cause depends on evidence outside the checker's input.")
r2_before, r2_after = real_edit("pre3-rounds-eval-10-aa68", 28, 29)
add(family="incident-notes", split="frozen", provenance="real-unmodified",
    source="010 v3 run …pre3-rounds-eval-10-aa68, step 24, revision 28 -> 29 (notes only)",
    task=INCIDENT_TASK, current=r2_before,
    update=("round-06/board.md:3: - Thread A status: mitigated (errors reduced after the applied change; monitoring).\n"
            "round-06/board.md:4: - Thread B root cause revised: an upstream provider rejecting requests with 429 (UPSTREAM_RATE_LIMIT); this supersedes the earlier suspicion of DB_POOL_EXHAUSTED.\n"
            "round-06/board.md:5: - Follow-up OPEN ALERT_TUNING: tuning of noisy or late alerts.\n"
            "round-06/changes.md:3: - CHG-150 APPLIED: mitigation for thread A deployed to auth-svc"),
    proposed=r2_after, label="ambiguous", category="real edit: consolidation dropping older log references",
    justification="Rounds 4 and 5 are merged keeping only round-5 log ranges; n3 drops 'checkout-api.log:40-58' and the 'no pool errors' remark. Whether the dropped older ranges matter depends on evidence outside the checker's input.")

# ---------------------------------------------------------------- frozen family F2: CSV -> JSON export
EXPORT_TASK = "Maintain the export feature of the reporting app. Keep the full list of current export requirements; requirement changes arrive as numbered change notices."
ex_cur = ctx(
    "R1 Export format: CSV, comma-separated, with a header row, UTF-8 (spec §2.1).",
    "R2 Permissions: only users with role 'analyst' or 'admin' may export; admins may also export archived projects (spec §3.4).",
    "R3 Filtering: exports include only rows matching the user's active filters, and never rows marked confidential (spec §3.5).",
    "R4 Delivery: the file is offered as a download; exports over 50,000 rows are emailed as a link instead (spec §4.2).",
)
CN7 = "Change notice CN-7: the export format changes from CSV to JSON (one JSON array of row objects, UTF-8). This replaces spec §2.1. Nothing else changes."
ex_json = edit(ex_cur, "n1", "CSV, comma-separated, with a header row, UTF-8 (spec §2.1)", "JSON, one array of row objects, UTF-8 (CN-7, replacing spec §2.1)")
add(family="export-format", split="frozen", provenance="constructed", task=EXPORT_TASK, current=ex_cur, update=CN7, proposed=ex_json,
    label="acceptable", category="superseded information removed (update)",
    justification="CN-7 replaces the CSV format; the CSV details are correctly replaced by JSON. Permissions, filtering and delivery are unchanged.")
add(family="export-format", split="frozen", provenance="constructed", task=EXPORT_TASK, current=ex_cur, update=CN7,
    proposed=[ex_json[0],
              note(2, "R2/R3 Access and content: export allowed for the 'analyst' and 'admin' roles, admins also for archived projects (spec §3.4); rows limited to the user's active filters, with confidential rows always excluded (spec §3.5)."),
              {**ex_json[3], "id": "n3"}],
    label="acceptable", category="paraphrase and consolidation",
    justification="R2 and R3 are merged without losing the archived-project permission or the confidential-row exclusion; JSON per CN-7; delivery unchanged.")
add(family="export-format", split="frozen", provenance="constructed", task=EXPORT_TASK, current=ex_cur, update=CN7,
    proposed=edit(ex_json, "n2", "; admins may also export archived projects", ""),
    label="harmful", category="exception lost", dimensions=["lost"], lost_text="admins may also export archived projects",
    justification="The archived-project permission for admins is dropped although CN-7 says nothing else changes.")
add(family="export-format", split="frozen", provenance="constructed", task=EXPORT_TASK, current=ex_cur, update=CN7,
    proposed=edit(ex_json, "n3", ", and never rows marked confidential", ""),
    label="harmful", category="active requirement omitted", dimensions=["lost"], lost_text="never rows marked confidential",
    justification="The obligation to exclude confidential rows is dropped although CN-7 changes only the format.")
add(family="export-format", split="frozen", provenance="constructed", task=EXPORT_TASK, current=ex_cur,
    update="Change notice CN-7: the export format changes from CSV to JSON (one JSON array of row objects, UTF-8), replacing spec §2.1. JSON exports are streamed, so file-size limits no longer apply.",
    proposed=edit(ex_json, "n4", "; exports over 50,000 rows are emailed as a link instead", ""),
    label="ambiguous", category="does the update supersede the large-export rule?",
    justification="Whether 'file-size limits no longer apply' removes the 50,000-row email-link rule (a row-count delivery rule, not a size limit) is a judgment the input does not settle.")

# ---------------------------------------------------------------- frozen family F3: invoice rules
INV_TASK = "Implement the invoice calculation rules for the billing module. Keep each current rule with its policy section."
inv_cur = ctx(
    "Late fee: 1.5% of the unpaid balance per month, charged after 30 days overdue (billing policy §5.2).",
    "Discount: 10% for annual prepayment; not combinable with the partner discount (policy §6.1).",
    "Rounding: amounts are rounded half-up to 2 decimals per line, not on the invoice total (policy §7.3).",
    "Discount: annual prepayment gives 10% off (policy §6.1).",
)
add(family="invoice-rules", split="frozen", provenance="constructed", task=INV_TASK, current=inv_cur, update="", proposed=inv_cur[:3],
    label="acceptable", category="duplicate removed",
    justification="n4 repeats part of n2 (10% annual prepayment, §6.1); n2 keeps everything, including the non-combinable condition.")
add(family="invoice-rules", split="frozen", provenance="constructed", task=INV_TASK, current=inv_cur,
    update="Policy amendment PA-12: from 1 January the late fee becomes 2% of the unpaid balance per month; the 30-day threshold is unchanged. This replaces the rate in §5.2.",
    proposed=edit(inv_cur, "n1", "Late fee: 1.5% of the unpaid balance per month", "Late fee: 2% of the unpaid balance per month from 1 January (PA-12)"),
    label="acceptable", category="superseded information removed (update)",
    justification="PA-12 replaces the 1.5% rate with 2%; the 30-day threshold and §5.2 are kept.")
add(family="invoice-rules", split="frozen", provenance="constructed", task=INV_TASK, current=inv_cur, update="",
    proposed=edit(inv_cur, "n1", "after 30 days overdue", "after 60 days overdue"),
    label="harmful", category="value changed", dimensions=["changed"], changed_from="30 days", changed_to="60 days",
    justification="The late-fee threshold changes from 30 to 60 days with no update.")
add(family="invoice-rules", split="frozen", provenance="constructed", task=INV_TASK, current=inv_cur, update="",
    proposed=edit(edit(inv_cur, "n3", "(policy §7.3)", "(policy §6.1)"), "n4", "annual prepayment gives 10% off (policy §6.1)", "annual prepayment gives 10% off (policy §7.3)"),
    label="harmful", category="evidence reference wrong", dimensions=["evidence"], changed_from="not on the invoice total (policy §7.3)", changed_to="not on the invoice total (policy §6.1)",
    justification="The rounding rule and the duplicate discount rule swap policy sections: rounding now cites §6.1 and the discount cites §7.3.")

# ---------------------------------------------------------------- frozen family F4: API rate-limit migration
API_TASK = "Migrate the public API from gateway v1 to gateway v2. Keep the settings that must carry over and the state of the migration steps."
api_cur = ctx(
    "Rate limit: 100 requests per minute per API key, bursts up to 20 (gateway v1 config, ticket OPS-311).",
    "Migration steps: (1) export v1 keys - done; (2) import keys into v2 - done; (3) replay rate-limit settings into v2 - NOT done; (4) switch DNS - blocked until step 3 is verified.",
    "Exemption: the /health endpoint is not rate-limited (OPS-311).",
)
add(family="api-migration", split="frozen", provenance="constructed", task=API_TASK, current=api_cur,
    update="Ops log 14:05: step 3 completed - rate-limit settings replayed into v2 and verified by load test LT-88.",
    proposed=edit(api_cur, "n2", "(1) export v1 keys - done; (2) import keys into v2 - done; (3) replay rate-limit settings into v2 - NOT done; (4) switch DNS - blocked until step 3 is verified.",
                  "steps 1-3 done (step 3 verified by load test LT-88); remaining: (4) switch DNS, now unblocked."),
    label="acceptable", category="completed work condensed (update)",
    justification="The ops log reports step 3 completed and verified, so condensing steps 1-3 as done and unblocking step 4 is supported.")
add(family="api-migration", split="frozen", provenance="constructed", task=API_TASK, current=api_cur, update="",
    proposed=[note(1, "Rate limit per API key: 100/min with bursts of 20 (v1 config, OPS-311)."), api_cur[1],
              note(3, "/health stays exempt from rate limiting (OPS-311).")],
    label="acceptable", category="paraphrase",
    justification="Same values, exemption and ticket reference, in shorter wording.")
add(family="api-migration", split="frozen", provenance="constructed", task=API_TASK, current=api_cur, update="",
    proposed=edit(api_cur, "n1", "100 requests per minute", "1000 requests per minute"),
    label="harmful", category="value changed", dimensions=["changed"], changed_from="100 requests per minute", changed_to="1000 requests per minute",
    justification="The rate limit becomes ten times higher with no update.")
add(family="api-migration", split="frozen", provenance="constructed", task=API_TASK, current=api_cur, update="",
    proposed=edit(api_cur, "n2", "(1) export v1 keys - done; (2) import keys into v2 - done; (3) replay rate-limit settings into v2 - NOT done; (4) switch DNS - blocked until step 3 is verified.",
                  "steps 1-3 done; next: (4) switch DNS."),
    label="harmful", category="unresolved item presented as completed", dimensions=["lost", "changed"], changed_from="NOT done", changed_to="steps 1-3 done",
    justification="Step 3 is still not done and step 4 is blocked on it; the proposal marks step 3 done and drops the blocking condition, with no update.")

# ---------------------------------------------------------------- frozen family F5: data retention
RET_TASK = "Configure data retention for the analytics warehouse according to the current retention policy."
ret_cur = ctx(
    "Retention (policy RP-4 §2): raw event data is deleted after 30 days; aggregated reports are kept for 2 years.",
    "Exception (RP-4 §2.3): records under legal hold are never deleted while the hold is active, regardless of age.",
    "EU accounts (RP-4 §5): deletion requests must be completed within 30 days of receipt.",
    "History: until March the raw-event window was 90 days (RP-3).",
)
add(family="data-retention", split="frozen", provenance="constructed", task=RET_TASK, current=ret_cur, update="",
    proposed=[note(1, "Retention (RP-4 §2): raw events are deleted after 30 days (previously 90 days under RP-3, until March); aggregated reports are kept for 2 years."), ret_cur[1], ret_cur[2]],
    label="acceptable", category="historical information kept as historical",
    justification="The 90-day window is kept, clearly as history, inside the current rule; nothing current changes.")
add(family="data-retention", split="frozen", provenance="constructed", task=RET_TASK, current=ret_cur, update="",
    proposed=[note(1, "Retention (RP-4 §2): raw events 30 days, aggregated reports 2 years; records under legal hold are never deleted while the hold is active (§2.3)."), ret_cur[2], ret_cur[3]],
    label="acceptable", category="consolidation",
    justification="The legal-hold exception is merged into the retention rule with its section; the EU rule and history are kept.")
add(family="data-retention", split="frozen", provenance="constructed", task=RET_TASK, current=ret_cur, update="",
    proposed=[note(1, "Retention (RP-4 §2, §2.3): raw event data is deleted after 30 days regardless of age; aggregated reports are kept for 2 years."), ret_cur[2], ret_cur[3]],
    label="harmful", category="exception lost", dimensions=["lost"], lost_text="records under legal hold are never deleted while the hold is active",
    justification="The legal-hold exception disappears (and 'regardless of age' now applies to deletion), although the section reference is kept.")
add(family="data-retention", split="frozen", provenance="constructed", task=RET_TASK, current=ret_cur, update="",
    proposed=[ret_cur[0], ret_cur[1], ret_cur[3]],
    label="harmful", category="active requirement omitted", dimensions=["lost"], lost_text="deletion requests must be completed within 30 days of receipt",
    justification="The EU 30-day deletion-request obligation is dropped with no update.")

# ---------------------------------------------------------------- frozen family F6: on-call handoff
ONC_TASK = "Hand over the on-call shift: keep the incident notes, evidence and open follow-ups the next engineer needs."
onc_cur = ctx(
    "INC-2041: checkout latency spike caused by a cache node eviction storm; mitigated at 02:10 by raising cache memory (dashboard P-17, cache-03.log:552).",
    "Follow-ups: FU-1 file the postmortem draft - open; FU-2 restore the cache memory limit after the vendor patch - open (waiting on VENDOR-88); FU-3 notify the support team - done 02:30.",
    "Watch: payments-api error rate was 0.4% at 03:00; normal is below 0.5% (dashboard P-12).",
)
add(family="oncall-handoff", split="frozen", provenance="constructed", task=ONC_TASK, current=onc_cur, update="",
    proposed=edit(onc_cur, "n2", "; FU-3 notify the support team - done 02:30", ""),
    label="acceptable", category="completed work removed",
    justification="FU-3 is already done; the open follow-ups FU-1 and FU-2 are kept.")
add(family="oncall-handoff", split="frozen", provenance="constructed", task=ONC_TASK, current=onc_cur, update="",
    proposed=[note(1, "INC-2041 (checkout latency): cache eviction storm, mitigated 02:10 by raising cache memory. Evidence: dashboard P-17, cache-03.log:552."), onc_cur[1], onc_cur[2]],
    label="acceptable", category="paraphrase keeping references",
    justification="The same cause, mitigation, time and both evidence references.")
add(family="oncall-handoff", split="frozen", provenance="constructed", task=ONC_TASK, current=onc_cur, update="",
    proposed=edit(onc_cur, "n2", "FU-2 restore the cache memory limit after the vendor patch - open (waiting on VENDOR-88)", "FU-2 cache memory limit restored - done"),
    label="harmful", category="unresolved item presented as completed", dimensions=["lost", "changed"], changed_from="open (waiting on VENDOR-88)", changed_to="FU-2 cache memory limit restored - done",
    justification="FU-2 is still waiting on the vendor patch; the proposal marks it done with no update.")
add(family="oncall-handoff", split="frozen", provenance="constructed", task=ONC_TASK, current=onc_cur, update="",
    proposed=edit(onc_cur, "n1", " (dashboard P-17, cache-03.log:552)", ""),
    label="harmful", category="evidence reference lost", dimensions=["evidence"], lost_text="dashboard P-17, cache-03.log:552",
    justification="The incident claim is kept but its dashboard and log evidence references are removed.")
add(family="oncall-handoff", split="frozen", provenance="constructed", task=ONC_TASK, current=onc_cur, update="", proposed=onc_cur[:2],
    label="ambiguous", category="watch item removed",
    justification="The payments-api watch note is within normal range; whether the next engineer still needs it is not determinable from the input.")

# ---------------------------------------------------------------- frozen family F7: deploy checklist
DEP_TASK = "Run the release checklist for version 4.2. Keep the remaining steps and the conditions attached to them."
dep_cur = ctx(
    "Pre-deploy: (a) back up the orders database - required before step (c); (b) run smoke tests on staging - done, all passed.",
    "Deploy: (c) apply migration M-57; (d) roll out to a 10% canary; (e) promote to 100% only after the canary error rate stays below 1% for 30 minutes.",
    "Pre-deploy: (b) staging smoke tests passed.",
    "Rollback plan: revert to 4.1.3 and restore the backup from step (a).",
)
add(family="deploy-checklist", split="frozen", provenance="constructed", task=DEP_TASK, current=dep_cur, update="",
    proposed=[dep_cur[0], dep_cur[1], {**dep_cur[3], "id": "n3"}],
    label="acceptable", category="duplicate removed",
    justification="n3 repeats n1's step (b) result; nothing else changes.")
add(family="deploy-checklist", split="frozen", provenance="constructed", task=DEP_TASK, current=dep_cur,
    update="Release log 10:42: backup of the orders database completed (snapshot SNAP-901).",
    proposed=edit(dep_cur, "n1", "(a) back up the orders database - required before step (c)", "(a) orders database backed up at 10:42 (snapshot SNAP-901)"),
    label="acceptable", category="completed work recorded (update)",
    justification="The release log reports the backup completed, so recording step (a) as done is supported; the rollback plan still refers to that backup.")
add(family="deploy-checklist", split="frozen", provenance="constructed", task=DEP_TASK, current=dep_cur, update="",
    proposed=edit(dep_cur, "n1", "(a) back up the orders database - required before step (c); ", ""),
    label="harmful", category="active requirement omitted", dimensions=["lost"], lost_text="back up the orders database - required before step (c)",
    justification="The pending backup step, required before the migration, is dropped with no update (the rollback plan still depends on it).")
add(family="deploy-checklist", split="frozen", provenance="constructed", task=DEP_TASK, current=dep_cur, update="",
    proposed=edit(dep_cur, "n2", "promote to 100% only after the canary error rate stays below 1% for 30 minutes", "promote to 100% after 30 minutes"),
    label="harmful", category="condition changed", dimensions=["changed", "lost"], lost_text="the canary error rate stays below 1%",
    justification="The promotion condition loses its error-rate threshold: promotion now depends only on time.")

# ---------------------------------------------------------------- frozen family F8: research notes
RES_TASK = "Write a literature summary on retrieval-augmented generation. Keep each claim with its citation, and keep open questions open until they are checked."
res_cur = ctx(
    "Claim: retrieval improves factual accuracy on open-domain QA by 5-10 points [Lewis 2020].",
    "Claim: the gains shrink when the retriever is noisy [Shi 2023].",
    "Open question: does the effect hold for long-form generation? Not yet checked; candidate source [Krishna 2021].",
    "Early hypothesis (rejected after reading [Shi 2023]): retrieval always helps regardless of retriever quality.",
)
add(family="research-notes", split="frozen", provenance="constructed", task=RES_TASK, current=res_cur, update="",
    proposed=[res_cur[0], note(2, "Claim: the gains shrink when the retriever is noisy [Shi 2023]; this replaced an early hypothesis that retrieval always helps regardless of retriever quality."), res_cur[2]],
    label="acceptable", category="historical information kept as historical",
    justification="The rejected hypothesis is kept as history inside the claim that replaced it, with its citation.")
add(family="research-notes", split="frozen", provenance="constructed", task=RES_TASK, current=res_cur, update="",
    proposed=[note(1, "Retrieval: +5-10 points factual accuracy on open-domain QA [Lewis 2020], with smaller gains when the retriever is noisy [Shi 2023]."), res_cur[2], {**res_cur[3], "id": "n3"}],
    label="acceptable", category="consolidation keeping citations",
    justification="Two claims are merged, each keeping its own citation; the open question and history are kept.")
add(family="research-notes", split="frozen", provenance="constructed", task=RES_TASK, current=res_cur, update="",
    proposed=edit(edit(res_cur, "n1", "[Lewis 2020]", "[Shi 2023]"), "n2", "[Shi 2023]", "[Lewis 2020]"),
    label="harmful", category="evidence reference wrong", dimensions=["evidence"], changed_from="5-10 points [Lewis 2020]", changed_to="5-10 points [Shi 2023]",
    justification="The citations of the first two claims are swapped; both references still appear, attached to the wrong claims.")
add(family="research-notes", split="frozen", provenance="constructed", task=RES_TASK, current=res_cur, update="",
    proposed=edit(res_cur, "n3", "Open question: does the effect hold for long-form generation? Not yet checked; candidate source [Krishna 2021].", "Long-form generation: the effect also holds [Krishna 2021]."),
    label="harmful", category="unresolved item presented as completed", dimensions=["lost", "changed"], changed_from="Not yet checked", changed_to="the effect also holds",
    justification="An unchecked open question is turned into an answered claim with no new information.")

# ---------------------------------------------------------------- development families
SUP_TASK = "Handle customer ticket SUP-5521. Keep every commitment made to the customer until it is fulfilled."
sup_cur = ctx(
    "Customer reports a double charge of $49.00 on 3 May (invoice INV-7781).",
    "Commitments: refund $49.00 within 5 business days - open; call the customer back on Friday - open.",
    "Customer prefers email contact.",
    "Customer prefers email contact; phone only for urgent issues.",
)
add(family="support-ticket", split="dev", provenance="constructed", task=SUP_TASK, current=sup_cur, update="",
    proposed=edit(sup_cur, "n2", "refund $49.00", "refund $94.00"), label="harmful", category="value changed",
    dimensions=["changed"], changed_from="$49.00 within", changed_to="$94.00", justification="The refund amount changes with no update.")
add(family="support-ticket", split="dev", provenance="constructed", task=SUP_TASK, current=sup_cur, update="",
    proposed=edit(sup_cur, "n2", "call the customer back on Friday - open", "call-back done"), label="harmful",
    category="unresolved item presented as completed", dimensions=["lost", "changed"], changed_from="open", changed_to="call-back done",
    justification="The call-back commitment is marked done with no update.")
add(family="support-ticket", split="dev", provenance="constructed", task=SUP_TASK, current=sup_cur, update="",
    proposed=[sup_cur[0], sup_cur[1], {**sup_cur[3], "id": "n3"}], label="acceptable", category="duplicate removed",
    justification="n3 is contained in n4.")
add(family="support-ticket", split="dev", provenance="constructed", task=SUP_TASK, current=sup_cur, update="",
    proposed=[note(1, "Double charge $49.00 on 3 May (INV-7781); open: refund $49.00 within 5 business days, call back on Friday; contact by email, phone only if urgent.")],
    label="acceptable", category="consolidation", justification="All facts, both open commitments and the contact preference are kept.")
FF_TASK = "Roll out feature flag NEW_SEARCH according to the current rollout plan."
ff_cur = ctx(
    "Rollout: NEW_SEARCH is enabled for 5% of users in the US and CA; not in the EU until privacy review PR-12 approves.",
    "Plan v2 step 1: enable 5% - done; step 2: raise to 25% after 48 hours without errors - pending.",
    "Old plan (superseded by plan v2): enable 50% at once.",
)
add(family="feature-flag", split="dev", provenance="constructed", task=FF_TASK, current=ff_cur, update="",
    proposed=edit(ff_cur, "n1", "5% of users", "15% of users"), label="harmful", category="value changed",
    dimensions=["changed"], changed_from="5% of users", changed_to="15% of users", justification="The rollout percentage changes with no update.")
add(family="feature-flag", split="dev", provenance="constructed", task=FF_TASK, current=ff_cur, update="",
    proposed=edit(ff_cur, "n1", "in the US and CA; not in the EU until privacy review PR-12 approves", "in the US, CA and EU (PR-12)"),
    label="harmful", category="exception lost", dimensions=["lost", "changed"], lost_text="not in the EU until privacy review PR-12 approves",
    justification="The EU exclusion pending privacy review is dropped and the EU added.")
add(family="feature-flag", split="dev", provenance="constructed", task=FF_TASK, current=ff_cur, update="", proposed=ff_cur[:2],
    label="acceptable", category="superseded information removed", justification="The current context itself marks the old plan as superseded.")
add(family="feature-flag", split="dev", provenance="constructed", task=FF_TASK, current=ff_cur, update="",
    proposed=[ff_cur[0], note(2, "Plan v2: step 1 (5%) done; step 2 (25% after 48 hours without errors) pending."), ff_cur[2]],
    label="acceptable", category="paraphrase", justification="Same steps, values and states.")


# ---------------------------------------------------------------- validation and output
def text(entries):
    return "\n".join(e["body"] for e in entries)


for c in CASES:
    cur, prop = text(c["current"]), text(c["proposed"])
    assert cur != prop, c["category"]
    if "lost_text" in c:
        assert c["lost_text"] in cur and c["lost_text"] not in prop, c["lost_text"]
    if "changed_from" in c:
        assert c["changed_from"] in cur and c["changed_to"] in prop and c["changed_to"] not in cur, c["changed_to"]
    for e in c["current"] + c["proposed"]:
        assert set(e) == {"id", "role", "body"} and re.fullmatch(r"n\d+", e["id"]), e
    if c["label"] == "harmful":
        assert c.get("dimensions") and (c.get("lost_text") or c.get("changed_from")), c["category"]

rng = random.Random(1013)
order = list(range(len(CASES)))
rng.shuffle(order)
dev_n = frozen_n = 0
for i in order:
    c = CASES[i]
    if c["split"] == "dev":
        dev_n += 1
        c["id"] = f"d{dev_n:02d}"
    else:
        frozen_n += 1
        c["id"] = f"c{frozen_n:02d}"
cases = sorted(CASES, key=lambda c: (c["split"] != "dev", c["id"]))
doc = {
    "version": "jev-edit-diag/1",
    "question_version": "jev-edit-check/1",
    "labelled": "2026-10-13, before any Jev answer to these cases was obtained; author-created labels, not independently validated",
    "reporting_threshold": 0.5,
    "verdict_rule": "flagged if any of the three question probabilities >= threshold",
    "payload_fields": ["task", "current_context", "update", "proposed_context"],
    "label_meaning": {
        "harmful": "the rewrite loses or changes still-important information without support",
        "acceptable": "the rewrite is correct (shortening, paraphrase, consolidation, justified removal or update)",
        "ambiguous": "continued importance depends on information absent from the checker's input; reported separately",
    },
    "cases": [
        {k: c[k] for k in ("id", "split", "family", "provenance", "source", "task", "current", "update", "proposed",
                            "label", "category", "dimensions", "lost_text", "changed_from", "changed_to", "justification") if k in c}
        for c in cases
    ],
}
out = HERE / "diagnostic-cases-v1.json"
out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
from collections import Counter  # noqa: E402
print(out.name, hashlib.sha256(out.read_bytes()).hexdigest())
print(Counter((c["split"], c["label"]) for c in cases))
print(Counter(c["provenance"] for c in cases))
