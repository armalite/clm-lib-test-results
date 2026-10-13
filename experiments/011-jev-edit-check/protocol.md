# 011 – Planned protocol: Jev check of a proposed context edit (strategy 3)

**Status: PLANNED. Not implemented, not run, and no paid calls are authorised.** Written on 2026-10-13 as part of the [roadmap](../jev-assistance-roadmap.md). Any implementation would first freeze a revised version of this protocol and a new diagnostic.

## Question

**Before Claude applies a context edit, does a Jev check for narrow, specific risks help Claude catch mistakes in the edit?**

## Design

**Both arms get a defined check opportunity.**
1. When Claude's code writes a `context.json` that is valid and **removes or rewrites** at least one entry, the runtime holds it as a *proposed* revision instead of committing it at once.
2. The next observation shows the proposed change: the removed and rewritten entries, before and after.
3. Claude replies `apply`, revises the edit, or withdraws it.

Edits that only add entries are committed as today.

**The arms:**
- **A (control):** the same check opportunity, without Jev.
- **B (assisted):** the same, plus Jev's answers to a few narrow questions about the proposed change.

**The Jev judgment, which is new and untested:** it differs from affected-entry detection, so **the 008/009 question is not assumed to work for it**. Candidate questions, each one narrow yes/no:
1. **Lost requirement:** per removed or rewritten entry, "Does the proposed revision omit a fact, requirement or planned action from this entry that no later update has superseded?"
2. **Stale carry-forward:** per kept or rewritten entry, "Does this entry still assert something that a recent update has superseded?" The recent updates would be the released payloads since the last check.

| | |
| --- | --- |
| **Trigger** | Every valid proposed edit that removes or rewrites entries |
| **Information: Claude** | Its context, the proposed diff, and (B) Jev's answers |
| **Information: Jev** | The old entry text, the proposed replacement text (or "removed"), and the recent released updates. Never future rounds, truth or deleted history beyond the entry being removed |
| **Who edits** | Claude: apply, revise or withdraw. Jev never approves or rejects |
| **Overhead** | One extra Claude turn per checked edit in **both** arms (pilot runs made 11–15 edits, so this could add about a third more calls), plus Jev calls in B |

## Possible failure modes

- **False alarms** cause churn: Claude revising correct edits.
- **Anchoring:** Claude applies everything Jev does not flag.
- **Compound questions:** "omits something still current" mixes recall with currency. This may need splitting.
- **Request size:** large rewrites may exceed batch limits.
- **Overhead in both arms** may dominate any benefit.

## Diagnostics before any agent run

- **A fresh labelled set**, for example `jev-diag/3`: (old entry, proposed revision, recent updates) triples, with labels for each question, written before any Jev answer.
- **Sources:** realistic edits taken from existing CLM traces, mutated to include both risks and correct edits.
- **Readiness:** the strategy is not ready for an agent pilot unless the component shows useful separation at a pre-fixed threshold.

## Outcomes

- **Primary:**
  - strict success, especially omissions and stale facts;
  - all-attempt cost.
- **Secondary:**
  - edits revised or withdrawn after the check in each arm;
  - calls and time added by the check;
  - Jev latency and cost.

## Limitations

- **The check opportunity itself is an intervention**, and its overhead is measured in both arms.
- **Scope:** the same task family and model as 009.
- **Not comparable across experiments:** results are not comparable with strategies 1 and 2 without a [common-workload comparison](../jev-assistance-roadmap.md#order-and-gating).

---

# Component diagnostic protocol (2026-10-13, session 8, written before any case labels, code or paid call)

_The planned design above is kept as written. This section covers **only** an offline-designed, live Jev **component diagnostic**. No agent integration, edit blocking or end-to-end run is part of it, and no main-model calls are authorised._

## Question

**Can Jev detect important information incorrectly lost or changed in a proposed context rewrite?**

- **Who does what:** Claude would propose the rewrite and Jev would check it. This is a checking intervention. It does not claim that Jev replaces Claude's reasoning, or that it reduces input cost.
- **Why test the component first:** experiments 009 and 010 found no benefit for affected-entry advice on the incident workload, and their failures were omissions and miscitations whose relation to context edits was **not** established.

## What Jev receives (one request per case)

**`state`:**

| Field | Content |
| --- | --- |
| `task` | The relevant task instructions the agent already has (a fixed per-family text) |
| `current_context` | The working-context entries before the rewrite (`id`, `role`, `body`), in order |
| `update` | An already released update needed to justify a change, or `""` if none |
| `proposed_context` | Claude's proposed replacement entries, in order |

**Never included:** labels, justifications, categories, family names, provenance, hidden answers, future requirements or evaluator data.
- **Neutral ids:** case ids are neutral (`c01`…, in a shuffled order) and are not sent; entry ids are ordinary (`n1`…).
- **No obligation list:** no extracted list of "critical obligations" is supplied. Jev must judge from the contexts alone.

## Judgments (`jev-edit-check/1`): three separate `noul` questions per case

1. **`lost`:** Does the proposed context drop, or mark as finished, an obligation, requirement, exception, open question or unresolved item that the current context still treats as active, when neither the current context nor the update says it is finished, superseded or no longer needed?
2. **`changed`:** Does the proposed context state a value, number, limit, condition, status or relationship differently from the current context, without the update or the current context supporting the change?
3. **`evidence`:** Does the proposed context remove the evidence reference supporting a claim it keeps, or attach a kept claim to a different reference than the current context did?

**Each question has fixed `true` and `false` criteria** (recorded verbatim in the code and in the freeze below). The criteria state explicitly:
- shortening, paraphrasing, merging and removing superseded, duplicated or completed items are **not** harmful;
- verbatim preservation is not required.

**Case verdict (predeclared):** *flagged* if **any** of the three probabilities is ≥ **0.5**, a reporting convention that is not tuned on frozen results.
- **Per-question results** are reported too. The three questions about one case are **not** independent examples.
- **Missing answers:**
  - a case where all three answers are missing, or the call failed after its retry, is **unanswered**;
  - partial answers use the available maximum and are reported as partial;
  - **for the gate, an unanswered harmful case counts as missed, and an unanswered acceptable case as falsely flagged.**

## Cases

**Labels:** **harmful**, a rewrite that loses or changes still-important information without support; **acceptable**, a correct rewrite; **ambiguous**, where continued importance depends on information absent from the checker's input, or reasonable readers would disagree. Ambiguous cases are reported separately.

**Development set:** **8 cases** from 2 families (customer support ticket; feature-flag rollout), 4 harmful and 4 acceptable. They are used only to check the API shape and the question wording; any wording change and every development call is recorded.

**Frozen set:** **32 labelled cases**, 16 harmful and 16 acceptable, from 8 further families (2 harmful + 2 acceptable each), **plus 4 ambiguous**.
- **The families:**
  - incident notes from real 010 v3 runs;
  - a CSV → JSON export change (the planned W2 workload's example);
  - invoice rules;
  - an API rate-limit migration;
  - data retention;
  - an on-call handoff;
  - a deploy checklist;
  - research notes with citations.
- **Harmful categories (16):**
  - an active requirement omitted (4);
  - an exception lost (2);
  - a value or condition changed (3);
  - a status changed without support (1);
  - an unresolved item presented as completed (3);
  - an evidence reference lost or wrong (3).
- **Acceptable categories (16):**
  - paraphrase or consolidation;
  - removal of superseded information (justified by the update);
  - removal of duplicated or completed work;
  - historical information kept as historical;
  - real edits.
- **Provenance, recorded per case:**
  - **`real-unmodified`:** a real 010 v3 edit, notes only;
  - **`real-altered`:** a real edit with a **deliberately injected** mistake, never described as an observed failure;
  - **`constructed`.**
- **Families are split** between the development and frozen sets.

**Labels and justifications are written before any Jev answer exists.**
- **Harmful cases** name the exact unsupported loss or change.
- **Acceptable cases** say why the rewrite is safe.
- **Programmatic validation:** the builder checks quoted values and references against the case text.
- **The labels are author-created**, not independently validated ground truth.

## Reference results

- **Always flag:** recall 16/16 with 16/16 false flags. This is the trivial reference.
- **Deterministic checks** (no semantics):
  - **D-ref:** any reference token (`file:line`, `§N`, ticket or change ids like `ABC-123`, `[Author Year]`) present in the current context but absent from the proposed one;
  - **D-num:** any number in the proposed context that appears in neither the current context nor the update;
  - **D-any:** D-ref or D-num.

  **What they catch:** dropped citations and invented numbers. **What they cannot judge:** whether a dropped item was still needed, or whether a change was justified.

Jev is useful here only if it adds judgment beyond these checks.

## Readiness gate (predeclared; engineering pilot-readiness only)

**On the 32 frozen labelled cases, Jev's case verdict must have:**
- **at least 14 of 16 harmful cases detected;**
- **at most 2 of 16 acceptable cases flagged;**
- **no material payload leakage or implementation defect.**

**Ambiguous cases do not count toward the gate.**

**Passing only supports considering an agent pilot.** It does not establish better task performance, lower cost or improved context management.

**If the gate fails:** the result is kept and the failure pattern explained, with **no automatic tuning cycle**. The frozen set is run **once**.

## Budget

- **Authorised:** up to **USD 3 of additional TypeSafe spend** for this diagnostic, including development calls and retries.
- **The ceiling** is set to the settled spend at the start + 3, replacing unused allowances.
- **Not authorised:** no main-model calls and no agent runs.

## Development run and question freeze (2026-10-13, before the frozen run)

**Development run:** `runs/jev-diagnostic/20261013T030359-edit-dev` (exported as a diagnostic).
- **Calls:** 8 requests and 8 attempts, with 0 errors, all answered by `jev-1.13.0`. The API accepted the object-valued state and the three noul questions with criteria.
- **Results:** 4/4 harmful detected and 0/4 acceptable flagged.
- **Latency and cost:** 0.25 s mean, 10,071 input tokens, USD 0.000421.
- **Changes after the development run:** **no wording change.** The question set below is the one used for development.

**Frozen settings:**
- **Question version:** `jev-edit-check/1` (SHA-256 of the question and criteria set, as sorted JSON: `c52a24b497f1226699109a3cd0d92e05a1572d88d0ff876d96e8cbfe6185461f`).
- **The scope instruction given with each question:** "Compare state.current_context (the working context before the rewrite) with state.proposed_context (the replacement). state.task is the task the context serves and state.update is already released information that may justify changes (empty if none)."
- **The questions and criteria** (verbatim):
- **`lost`:** Does the proposed context drop, or mark as finished, an obligation, requirement, exception, open question or unresolved item that the current context still treats as active, when neither the current context nor the update says it is finished, superseded or no longer needed?
  - **true:** Yes if an item that is still active in the current context is missing from the proposed context, or is now described as done, closed, answered or no longer applicable, and neither the current context nor the update supports that. This includes losing an exception or condition attached to a requirement that is kept.
  - **false:** No if every active item is still present, possibly paraphrased, shortened or merged; if removed items were superseded, completed, duplicated or closed according to the current context or the update; or if historical information is kept as history. A shorter context is not by itself a loss.
- **`changed`:** Does the proposed context state a value, number, limit, condition, status or relationship differently from the current context, without the update or the current context supporting the change?
  - **true:** Yes if a value, threshold, amount, date, percentage, status, scope or which-applies-to-what relationship differs from the current context and the update does not justify the new version.
  - **false:** No if values, conditions and statuses mean the same (wording may differ), or if every difference is justified by the update or by the current context itself.
- **`evidence`:** Does the proposed context remove the evidence reference supporting a claim it keeps, or attach a kept claim to a different reference than the current context did?
  - **true:** Yes if a claim that remains in the proposed context had a source reference (file:line, document section, ticket, dashboard, link or citation) in the current context and that reference is now missing, or the claim now cites a different reference without the update supporting it.
  - **false:** No if kept claims keep their references (possibly reformatted or merged), if a claim and its reference were removed together, or if a reference changed in a way the update supports.
- **Model and API:** `jev-1.13.0` (pinned) at `https://api.typesafe.ai/v1/systemone`; a 15 s timeout and 1 runtime retry for 429/529/5xx/timeouts, with no hidden retries. Each attempt is reserved and settled in the ledger as kind `jev-diagnostic`.
- **Cases:** `diagnostic-cases-v1.json`, SHA-256 `1d54373555eb339b374016671afdb27f8014942dbbe7014a06ec61e596ebfe78`. The frozen split has 16 harmful, 16 acceptable and 4 ambiguous cases.
- **Scoring:**
  - **Threshold:** 0.5; flagged if **any** question reaches it.
  - **Missing answers:** a case with all answers missing (or a failed call) is unanswered and counts as missed if harmful, or flagged if acceptable. A partial case uses the available maximum.
- **Reported:**
  - detections, misses and false flags with raw counts, precision and recall;
  - per question and per category;
  - the ambiguous cases separately;
  - the always-flag and deterministic references;
  - latency, tokens, cost and errors.
- **Gate:** at least 14/16 harmful detected, at most 2/16 acceptable flagged, and no leakage or defect. The frozen set is run **once**.

## Frozen run result record (2026-10-13)

- **The run:** `runs/jev-diagnostic/20261013T030432-edit-frozen`, executed **once** with the frozen question and cases. 36 requests and attempts, 0 errors, 0 unanswered, all answered by `jev-1.13.0`, at 0.24 s mean and USD 0.002213.
- **Gate:** harmful detected **16/16** (passes ≥ 14); acceptable flagged **3/16** (**fails** ≤ 2); no leakage or defect. **The gate FAILED.**
- **False flags:** `c02` (a completed follow-up removed; `changed` 0.70), `c29` (a real edit adding log findings; `changed` 0.60) and `c27` (a real edit replacing older log ranges with newer ones; `evidence` 0.58).
- **Ambiguous cases:** 0.64, 0.62, 0.63 and 0.45.
- **Deterministic reference D-any:** 7/16 recall with 3/16 false flags, on the same three cases.
- **As this protocol requires:** the result is kept; the threshold, question and labels are unchanged; the frozen set is not rerun; and no tuning cycle or agent pilot was started.
- **Spend:** USD 0.002634 in total (development and frozen runs), TypeSafe only. The ledger is at USD 82.005891 of USD 85.003257.

---

# Component diagnostic v2: evidence-complete checking (2026-10-13, written before any v2 code, cases or paid call)

_v1 (the protocol, cases `diagnostic-cases-v1.json`, results and the failed gate) is preserved unchanged. v2 uses **fresh** cases, a versioned evidence contract and versioned questions, and is exported as separate diagnostics. Diagnosis of v1's false alarms: [`analysis/v1-false-alarm-diagnosis.md`](analysis/v1-false-alarm-diagnosis.md)._

## Scope

- **What it is:** a checker component only. **The ordinary CLM runtime is unchanged:** model-written code edits the live working-context file, and that file determines later requests.
- **What it is not:** no review workflow, edit holding or blocking is added, and no agent run or main-model call is made.

## Evidence contract (`edit-evidence/1`)

The contract is what a real checker could receive at the moment a proposed `context.json` has been written and before the runtime accepts it. It is assembled by one deterministic function, `select_evidence()` in clm-lib, from **case inputs that mirror runtime state**. It uses no labels, no evaluator knowledge, and no hand-picked support.

| Field | Content | Rule and limits |
| --- | --- | --- |
| `task` | Task instructions already visible to the agent | As given |
| `current_context` | **All** entries of the current revision, in order: notes, tool observations still in context, step actions and receipts | Each body is cut at 6,000 characters (the runtime's output cap) with an explicit marker |
| `update` | Already released updates that the case's task declares (for example the latest round's board and change-log lines), or `""` | As given; cut at 4,000 characters with a marker |
| `execution_output` | stdout of the execution that wrote the proposal. The runtime captures it **before** it reads back and validates `context.json`, so the code is never executed twice | Cut at 6,000 characters with a marker; `""` if nothing was printed |
| `cited_sources` | For every `path:lines` reference that appears in `proposed_context` but not verbatim in `current_context`, the exact cited lines from the **released source files** that remain accessible to the agent | At most 20 lines per reference and 300 characters per line, and 8,000 characters in total; ranges longer than 20 lines are cut |
| `evidence_notes` | An explicit list of everything missing or truncated: unresolvable references (an unknown path, a missing line, an ambiguous short path), truncations, and "no execution output" | Always present (empty if complete) |
| `proposed_context` | The proposed replacement entries, in order | Each body is cut at 6,000 characters with a marker |

**What is excluded:**
- deleted context revisions;
- future or unreleased evidence;
- internal reasoning;
- unprinted intermediate values;
- labels, categories, provenance and justifications.

A proposal that relies on uncaptured evidence is an **information gap**. It shows up as missing support and in `evidence_notes`; it is never filled in from evaluator knowledge.

**Feasibility in the runtime (documented, not built):**
- **Already available:** all fields exist at the proposal point. `current_context` is `store.current`, `execution_output` is the `ExecResult.stdout` captured before `read_back`, and the released fixtures are on the host.
- **What an integration would add:** a `select_evidence` call between execution and `read_back`, plus the proposed entries parsed from the workspace file.
- **Not covered:** evidence the agent saw in an earlier step and then **deleted from context** stays out of reach unless the agent cites a source line. This limit is reported, not worked around.

## Questions (`jev-edit-check/2`): four `noul` questions per case

1. **`lost`:** whether the proposal drops, or marks as finished, an item that is still active, without support. The v1 meaning is kept.
2. **`changed`:** whether it states existing content differently without support. The criteria now say that **removing** an item is judged only by `lost`, and that new content supported by the supplied evidence is not an unsupported change.
3. **`evidence`:** whether it loses or reassigns the reference of a kept claim. The v1 meaning is kept.
4. **`insufficient`** (new): whether the supplied material is **insufficient to check** the proposal's new or changed content. This asks for an abstention signal, **not** a harm judgment: "not justified by the supplied material" does not mean "factually wrong".

**The exact texts** are recorded at the freeze. Every question refers to the evidence fields explicitly.

## Verdict rule (`edit-verdict/2`)

**Per case, at the reporting threshold of 0.5** (kept from v1; **not** re-chosen from v1's score separation):
- **flagged** if `lost`, `changed` or `evidence` ≥ 0.5;
- otherwise **uncertain** (abstain) if `insufficient` ≥ 0.5;
- otherwise **clear**.

**Unanswered cases:** every answer missing, or the call failed after its retry.

**Counting:**
- **Harmful cases:** only *flagged* counts as detected. **Uncertain or unanswered counts as not detected.**
- **Acceptable cases:** only *clear* counts as approved. *Flagged* is a false alarm, and *uncertain* or unanswered means the case would still need inspection.

## Cases

**Fresh families** with no paraphrases of v1's families. Related examples stay in one split, and labels and justifications are written before any answer.
- **Development:** 8 cases (4 harmful, 4 acceptable) from 2 families of their own, used only to check the contract, the payload size and the wording. Any wording change is recorded.
- **Frozen:** **16 harmful and 16 acceptable** from 8 families (2 + 2 each), **plus at least 4 insufficient-evidence or ambiguous cases** reported separately.
  - **Acceptable cases:** rewrites supported by supplied tool observations or cited lines; safe paraphrase; removal of obsolete or completed information.
  - **Harmful cases:** errors despite superficially related supporting material; lost exceptions and obligations; lost or reassigned evidence; and changing-requirements cases from the planned W2 workload.
  - **Real edits from 010 v3 runs:** included with their **full** current revision, either unmodified or deliberately altered (injected faults are labelled as such). They use different edits from v1's.
- **Every unambiguous case must be judgeable from the exact payload.** Cases that depend on uncaptured evidence go in the insufficient-evidence group.

## Readiness gate (predeclared)

**On the 32 frozen labelled cases, all of the following are required:**

| Criterion | Requirement |
| --- | --- |
| Harmful cases *flagged* | at least **14 / 16** |
| Acceptable cases *flagged* (false alarms) | at most **2 / 16** |
| **Coverage:** acceptable cases *clear* | at least **12 / 16**, so at most 4 acceptable cases may need inspection (flagged, uncertain or unanswered) |
| Leakage or material implementation defect | none |

**Reported separately:** the insufficient-evidence and ambiguous group. The desired outcome there is *uncertain*, or *flagged* if the gap hides a harm, but they are not in the gate.

**Passing only supports considering an agent pilot.**

**The frozen set is run once.** If the gate fails, the result is kept and explained, with no automatic tuning cycle.

## Reference checks (given the same evidence)

- **D-ref:** a reference token in the current context that is missing from the proposal.
- **D-num:** a number in the proposal that appears in none of the current context, the update, the execution output or the cited sources.
- **D-any:** D-ref or D-num.
- **Always flag.**
- **Their limits:** they cannot judge whether a loss matters, or whether supplied text actually supports a claim.

## Budget

- **Authorised:** up to **USD 3 of TypeSafe spend** for v2, including development calls and retries.
- **The ceiling** is set to the settled spend at the start + 3, replacing unused allowances.
- **Not authorised:** no main-model calls and no agent runs.

## v2 cases built (2026-10-13, before any v2 Jev answer)

- **File:** `diagnostic-cases-v2.json` (`jev-edit-diag/2`), SHA-256 `384feb4221d3baeb19d54068c0cbe36238e715e816bd4a00dd5d4eb7bf29597c`, built by `diagnostic-cases-v2.build.py`, which also validates the quoted strings mechanically. Labels and justifications were written before any v2 answer existed.
- **Development (8):** 4 harmful and 4 acceptable, from 2 families (trip itinerary; grading rubric with a W2-style weight change).
- **Frozen (38):** 16 harmful and 16 acceptable from 8 families with 2 + 2 each:
  - real incident edits from 010 v3 ordinary-CLM runs, with the full current revision;
  - a notification channel switch (W2-style);
  - a dependency upgrade with test output;
  - a schema migration;
  - security findings;
  - meeting action items;
  - lab measurements;
  - a payout export format change (W2-style).

  Plus **6 gap cases** (5 `insufficient`, 1 `ambiguous`), reported separately.
- **Provenance:** 41 constructed, 2 real-unmodified (both acceptable), 3 real-altered (2 harmful with an injected mistake, 1 insufficient with an injected unsupported claim). **The injected mistakes are not failures observed in agent runs.**
- **Fresh families:** none paraphrases a v1 family. The incident-real cases use two different 010 v3 runs and steps from v1's.
- **Judgeability check** (before any answer): `select_evidence` was run over every case.
  - Every unambiguous case's support or contradiction lies in the payload: a context observation, the execution output, or a newly cited source line.
  - One acceptable case whose support was only in an already-cited, unfetched line was given execution output showing that line before any answer.
  - Two real cases (one acceptable, one harmful) disclose an unresolvable short path (`ledger-svc.log:14-31` exists in several rounds); their support is in a context observation.
  - Two gap cases disclose their gap in `evidence_notes` (an unreleased file; a cited range beyond the 20-line limit). The other three gap cases have none to disclose: an unprinted computation, deleted context, and a claim with no source.
- **Leakage scan:** across all 46 request bodies, no label, category, family, id, provenance, justification or words such as "injected" appear.

## v2 development run 1 and one wording correction (2026-10-13)

**Run `20261013T033931-edit2-dev`** (8 dev cases, draft wording, USD 0.000562, 0 errors):
- **Harmful:** 4/4 flagged.
- **Acceptable:** 3/4 clear, 1/4 flagged. **`v01`:** the open "book a hotel" item was closed, citing a newly cited hotel-confirmation line. `lost` scored exactly 0.50.

**Cause found:** the draft reused v1's `lost` question and criteria, and v1's `changed` question text and `evidence` criteria. These name only "the current context or the update" as allowed support. So completion, change or re-citation justified by **execution output or cited sources** (the material the v2 evidence contract adds) fell outside the wording. This is an inconsistency between the questions and the evidence contract, not a threshold matter.

**Correction:**
- **The wording fix:** in the `lost` question and both criteria, the `changed` question text, and the `evidence` true/false criteria, "the update" or "the current context or the update" is replaced by "the supplied material (current context, update, execution output or cited sources)".
- **Unchanged:** nothing else, including the `changed` criteria, the `insufficient` question, the scope text, the verdict rule, the threshold and the cases.
- **Tests:** a new test checks that every harm question names execution output and cited sources.
- **Run records:** v2 summaries now record `questions_sha256`, a fingerprint of the exact scope and question texts. Dev run 1 predates it; its exact draft texts are in its request files.

**Decision rule, set before re-running:**
- **The rerun:** the development split is run **once more** with the corrected wording, to check the change on the development cases.
- **No further wording changes** follow that run, whatever it shows, unless it reveals an implementation defect.
- **Then the freeze.**

## v2 development run 2 and freeze (2026-10-13, before the frozen run)

**Run `20261013T034105-edit2-dev`** (corrected wording, `questions_sha256` `8ad0d68a86c4a47eb7a3489e210fbdce607c3aa3b61f1aa1e9ee54d1cc67df83`):
- **Results:** 4/4 harmful flagged and 4/4 acceptable clear.
- **`v01`:** `lost` 0.35 (was 0.50).
- **Cost and errors:** USD 0.000582, 0 errors.

No further wording change is made, as decided before this run.

**Frozen for the single frozen run:**
- **Evidence rule:** `edit-evidence/1`, as in the contract table above.
- **Limits:**
  - entries 6000 characters each;
  - update 4000;
  - execution output 6000;
  - 20 lines per cited reference, 300 characters per line, 8000 cited characters in total.

  Truncation and unresolved references are disclosed in `evidence_notes`.
- **Questions:** `jev-edit-check/2`, `questions_sha256` `8ad0d68a86c4a47eb7a3489e210fbdce607c3aa3b61f1aa1e9ee54d1cc67df83`; the verbatim texts are below.
- **Verdict:**
  - `edit-verdict/2`: *flagged* if any of `lost`, `changed` or `evidence` ≥ 0.5;
  - otherwise *uncertain* if `insufficient` ≥ 0.5;
  - otherwise *clear*;
  - *unanswered* if no answer came back.

  The threshold is **0.5**, not re-chosen from v1's separation.
- **Model and API:** `jev-1.13.0`, `https://api.typesafe.ai/v1/systemone`, `noul` questions, 15 s timeout, 1 runtime retry (429/529/5xx/timeouts), with each attempt in the ledger. Config: `configs/exp011v2.toml`. The implementation file's SHA-256 at the freeze is `c1d4034deddf20a588dd36665aa4e4ac79fded1a9c69172ada77eff881b29be4`.
- **Cases:** `diagnostic-cases-v2.json`, SHA-256 `384feb4221d3baeb19d54068c0cbe36238e715e816bd4a00dd5d4eb7bf29597c`.
  - **Frozen split:** 16 harmful, 16 acceptable, 5 insufficient, 1 ambiguous.
  - **Labels and provenance** are as in the file.
- **Metrics:**
  - harmful flagged, uncertain or clear;
  - acceptable clear, flagged or uncertain (and so needing inspection);
  - the per-question counts;
  - the gap-case verdicts, reported separately;
  - Wilson 95% intervals in the write-up;
  - D-ref, D-num, D-any and always-flag, given the same evidence;
  - latency, tokens and cost.
- **Gate:**
  - harmful flagged ≥ 14/16;
  - acceptable flagged ≤ 2/16;
  - acceptable clear ≥ 12/16;
  - no leakage or material implementation defect.
- **The frozen split is run once.** Errors are retried only by the runtime retry above, with no rerun of the split.

**Verbatim scope and questions (`jev-edit-check/2`):**

```json
{
 "scope": "Compare state.current_context (the full working context before the rewrite, including tool observations still in it) with state.proposed_context (the replacement). The supporting material is state.update (already released information), state.execution_output (what the code that wrote the proposal printed), state.cited_sources (the exact source lines for references newly cited in the proposal) and state.current_context itself. state.evidence_notes lists anything missing or truncated. state.task is the task the context serves.",
 "questions": {
  "lost": {
   "question": "Does the proposed context drop, or mark as finished, an obligation, requirement, exception, open question or unresolved item that the current context still treats as active, when nothing in the supplied material (current context, update, execution output or cited sources) says it is finished, superseded or no longer needed?",
   "criteria": {
    "true": "Yes if an item that is still active in the current context is missing from the proposed context, or is now described as done, closed, answered or no longer applicable, and nothing in the supplied material (current context, update, execution output or cited sources) supports that. This includes losing an exception or condition attached to a requirement that is kept.",
    "false": "No if every active item is still present, possibly paraphrased, shortened or merged; if removed items were superseded, completed, duplicated or closed according to the supplied material (current context, update, execution output or cited sources); or if historical information is kept as history. A shorter context is not by itself a loss."
   }
  },
  "changed": {
   "question": "Does the proposed context state a value, number, limit, condition, status or relationship differently from the current context, without the supplied material (current context, update, execution output or cited sources) supporting the change?",
   "criteria": {
    "true": "Yes if a value, threshold, amount, date, percentage, status, scope or which-applies-to-what relationship that the proposed context states differs from what the current context states, and the supplied material does not justify the new version, or the supplied material contradicts it.",
    "false": "No if values, conditions and statuses mean the same (wording may differ); if every difference is justified by the supplied material; or if content was only removed (removal is judged by a separate question, not as a change). New content that the supplied material supports is not an unsupported change."
   }
  },
  "evidence": {
   "question": "Does the proposed context remove the evidence reference supporting a claim it keeps, or attach a kept claim to a different reference than the current context did?",
   "criteria": {
    "true": "Yes if a claim that remains in the proposed context had a source reference (file:line, document section, ticket, dashboard, link or citation) in the current context and that reference is now missing, or the claim now cites a different reference without the supplied material (current context, update, execution output or cited sources) supporting it.",
    "false": "No if kept claims keep their references (possibly reformatted or merged), if a claim and its reference were removed together, or if a reference changed in a way the supplied material (current context, update, execution output or cited sources) supports."
   }
  },
  "insufficient": {
   "question": "Is the supplied material insufficient to check whether the proposed context's new or changed content is supported?",
   "criteria": {
    "true": "Yes if the proposed context adds or changes content whose support would have to come from material that is not supplied: for example state.evidence_notes reports the relevant material as missing or truncated, or a new claim has no checkable source in the current context, update, execution output or cited sources.",
    "false": "No if every addition or change can be checked against the supplied material (whether or not it turns out to be supported), or if the proposal only removes, merges or rephrases existing content."
   }
  }
 }
}
```

## v2 result record (2026-10-13, written after the single frozen run)

**Run `20261013T034139-edit2-frozen`** (run once):
- **Calls:** 38 requests and 38 attempts, **0 errors**, 0 unanswered, all answered by `jev-1.13.0`.
- **Usage:** 80,548 input and 2,774 output tokens (about 2,120 input tokens per check).
- **Latency:** 0.24 s mean (max 0.29 s).
- **Cost:** USD 0.003385.

**Gate** (32 labelled cases):

| Criterion | Required | Result |
| --- | --- | --- |
| Harmful flagged | ≥ 14/16 | **16/16: passed** |
| Acceptable flagged | ≤ 2/16 | **1/16: passed** |
| Acceptable clear (coverage) | ≥ 12/16 | **15/16: passed** |
| Leakage or defect | none | none found (leak scan 0; leak and evidence tests pass; 0 errors) |

**The readiness gate PASSED.**

**Further results:**
- **Harmful cases:** 0 uncertain and 0 clear.
- **Acceptable cases:** 0 uncertain; 1/16 needs inspection (`k03`, flagged).
- **Gap cases (not in the gate):** all 6 were flagged.
  - **The 5 `insufficient` cases:** `insufficient` scored 0.91–0.96, but `changed` also scored 0.90–0.97, so under edit-verdict/2's harm precedence none came out as *uncertain*.
  - **The ambiguous case:** `lost` scored 0.95.
- **Recorded unchanged.** Nothing was rescored, relabelled or rerun.
