# 011 – Can Jev check a proposed context rewrite? (component diagnostic)

**Status (component diagnostics only, no agent integration):**
- **v1** (`jev-edit-check/1`): **readiness gate FAILED.** 16/16 harmful detected, but 3/16 acceptable flagged (the maximum was 2).
- **v2** (`jev-edit-check/2`, evidence-complete): **readiness gate PASSED.** On a fresh frozen set, 16/16 harmful were flagged, 1/16 acceptable flagged and 15/16 acceptable clear.

**Not done:** no agent integration, edit blocking or end-to-end run was built or run, and no main-model calls were made.

**Context:** part of the [Jev-assistance roadmap](../jev-assistance-roadmap.md). Protocol: [`protocol.md`](protocol.md), which has v1's sections, then v2's:
- the contract, written before any v2 code or case;
- the case build;
- development runs 1 and 2;
- the freeze;
- the result record.

**What 011 tests.** In ordinary CLM, Claude edits its live context file by writing code. 010's mandatory reviews were experimental restrictions on that. **011 tests only a checker:** given a proposed rewrite and the evidence a runtime could supply, can Jev tell harmful rewrites from acceptable ones? Nothing here adds a review workflow to CLM.

## v2: evidence-complete checking (2026-10-13)

### Why v1's false alarms happened

[`analysis/v1-false-alarm-diagnosis.md`](analysis/v1-false-alarm-diagnosis.md) (exploratory; v1 is not rescored):
- **`c29` and `c27`, real edits:** their new content was supported by tool output still in the agent's context (the step-9 and step-29 observations). **v1's case construction kept only the note entries**, so the checker never saw that evidence. This is missing evidence introduced by the cases, not an error in Jev's reading.
- **`c02`:** removing a follow-up the context marked "done" was scored by `changed` (0.70). The question wording misclassified a removal as a change.

### The evidence contract (`edit-evidence/1`)

Each check sends Jev one state, built **mechanically** by `select_evidence()` from what a runtime has at edit time:

| Field | Content | Limit |
| --- | --- | --- |
| `task` | the task instructions | — |
| `current_context` | **every entry of the current revision**, including tool observations and receipts still in context | 6,000 characters per entry |
| `update` | the released update (board and change lines), if any | 4,000 |
| `execution_output` | stdout of the execution that wrote the proposal (no second execution) | 6,000 |
| `cited_sources` | the exact lines for `path:lines` references **newly cited** in the proposal, read from released files only | 20 lines per reference, 300 characters per line, 8,000 in total |
| `evidence_notes` | every truncation, missing output, and unresolved or ambiguous reference | — |
| `proposed_context` | the replacement entries | 6,000 per entry |

**Never supplied:**
- deleted revisions;
- unreleased files;
- whole source files;
- labels, ids, families or provenance.

**Truncation** is marked in the text and listed in `evidence_notes`.

**Feasibility:**
- **The inputs exist at edit time.** The runtime already holds every input:
  - the current revision (the `ContextStore`);
  - released stages;
  - the proposing execution's stdout;
  - the released fixtures.
- **Not built:**
  - holding a written `context.json` as a proposal instead of committing it at read-back;
  - passing those inputs to `select_evidence`.

  Both are documented in the clm-lib architecture notes, not built.
- **Cost of a check:** 0.5–8.7 KB of state (about 2,100 input tokens), 0.24 s and USD 0.00009 on these cases.
- **A known limit:** references are resolved only by exact path or a unique path suffix. On one real edit, the agent's short path `ledger-svc.log:14-31` exists in three rounds. It was reported as ambiguous, not guessed.

### Questions and verdicts

**`jev-edit-check/2`:** four `noul` questions, with the verbatim texts in the protocol freeze (`questions_sha256` `8ad0d68a…`):
- **`lost`, `changed`, `evidence`:** v1's three harm questions, now saying support may come from **any supplied material** (current context, update, execution output or cited sources).
  - `changed`'s criteria also say that removal is judged by `lost`, not as a change.
- **`insufficient`:** whether the supplied material is insufficient to check the new or changed content.

**`edit-verdict/2`:**
- **flagged** if any harm answer ≥ **0.5**;
- otherwise **uncertain** if `insufficient` ≥ 0.5;
- otherwise **clear**;
- **unanswered** if nothing came back.

**Uncertain is not clear:** an acceptable case that is not *clear* needs inspection, and a harmful case that is *uncertain* is not a detection. The threshold is the predeclared 0.5, not re-chosen from v1.

**One wording correction during development (disclosed):** in development run 1, the draft still named only "the current context or the update" as support in the harm questions. One acceptable development case, an open item closed by a newly cited confirmation line, scored `lost` 0.50.
- **The correction:** "the supplied material (…)" was substituted in those places. A test now checks that the questions name all four sources.
- **The decision rule,** set before re-running: one more development run, then a freeze regardless. Run 2 was clean, so the wording froze.

### The cases (`diagnostic-cases-v2.json`, `jev-edit-diag/2`)

**Built by:** [`diagnostic-cases-v2.build.py`](diagnostic-cases-v2.build.py), which validates the quoted strings and references mechanically. SHA-256 `384feb42…597c`.
- **Labels and justifications** were written before any v2 answer. They are author-created, not independently validated.
- **Fresh families:** none paraphrases v1, and related cases share a split.

| Set | Harmful | Acceptable | Gap cases | Families |
| --- | --- | --- | --- | --- |
| Development | 4 | 4 | — | trip itinerary; grading rubric (W2-style weight change) |
| Frozen | 16 | 16 | 5 insufficient, 1 ambiguous | real 010 incident edits (full revision); notification channel switch (W2); dependency upgrade with test output; schema migration; security findings; meeting actions; lab measurements; payout format change (W2); plus latency-report and config-audit gap cases |

**What the cases cover:**
- acceptable rewrites supported by a context observation, execution output or a newly cited line;
- harmful rewrites made despite superficially related material (failing tests reported as "passing", a citation moved to another log with the same line numbers, a CVE marked fixed while the rescan still lists it);
- safe paraphrase, consolidation and removal of completed items;
- lost exceptions, obligations and evidence;
- changing requirements.

**Provenance:**
- **Constructed:** 41 cases.
- **Real-unmodified (2):** ordinary-CLM edits from 010 v3, both acceptable.
- **Real-altered (3):** two harmful and one insufficient, each with a **deliberately injected** mistake. **These are not failures observed in agent runs.**

**Checks made before any answer:**
- **Judgeability:** every unambiguous case's support or contradiction lies in the exact payload. `select_evidence` was run over every case.
- **Leakage:** a scan of all 46 request bodies found no label, category, family, id, provenance or justification text.

### v2 results

**The frozen run (`20261013T034139-edit2-frozen`, run once):**
- **Calls:** 38 requests, 0 errors.
- **Latency:** 0.24 s mean (max 0.29 s).
- **Cost:** USD 0.003385.

The intervals below are Wilson 95% intervals.

| On the 32 labelled frozen cases | Jev v2 | Always flag | D-ref | D-num | D-any |
| --- | --- | --- | --- | --- | --- |
| **Harmful flagged** | **16/16** [0.81, 1.00] | 16/16 | 9/16 | 2/16 | 11/16 [0.44, 0.86] |
| Harmful uncertain | 0/16 | — | — | — | — |
| Harmful clear (missed) | 0/16 | 0/16 | 7/16 | 14/16 | 5/16 |
| **Acceptable clear (coverage)** | **15/16** [0.72, 0.99] | 0/16 | 9/16 | 15/16 | 8/16 |
| **Acceptable flagged** | **1/16** [0.01, 0.28] | 16/16 | 7/16 | 1/16 | 8/16 [0.28, 0.72] |
| Acceptable uncertain | 0/16 | — | — | — | — |
| **Acceptable needing inspection** | **1/16** | 16/16 | 7/16 | 1/16 | 8/16 |

- **The deterministic checks got the same evidence.** D-num accepts numbers from the execution output and cited sources.
- **D-ref is worse on full revisions:** removing a processed tool observation removes the paths printed in it.

**Per question** (answers within one case are not independent):

| Question | Harmful ≥ 0.5 | Acceptable ≥ 0.5 |
| --- | --- | --- |
| `lost` | 12/16 | 0/16 |
| `changed` | 12/16 | 0/16 |
| `evidence` | 6/16 | 1/16 |
| `insufficient` | 5/16 | 1/16 (also 5/5 insufficient cases) |

**Separation (observation only; no threshold change):**
- **The weakest harmful cases:** the lowest harmful maximum harm score was 0.60 (`k08`), then 0.74 (`k05`, `k31`).
- **The highest acceptable scores:** 0.56 (`k03`), then 0.41.
- **The margin is narrower than v1's** (0.83 vs 0.70).

**Gap cases (not in the gate): all 6 flagged, none uncertain.**

| Case | Gap | `insufficient` | Highest harm answer |
| --- | --- | --- | --- |
| `k20` | cites an unreleased file (disclosed in `evidence_notes`) | 0.96 | `changed` 0.96 |
| `k23` | value from an unprinted computation | 0.95 | `changed` 0.93 |
| `k25` | support lies beyond the 20-line cut (disclosed) | 0.94 | `changed` 0.97 |
| `k29` | real edit with an injected claim that has no captured source | 0.91 | `changed` 0.90 |
| `k36` | claim relying on deleted context | 0.95 | `changed` 0.94 |
| `k07` (ambiguous) | pending check removed without a stated reason | 0.27 | `lost` 0.95 |

**`insufficient` recognised every evidence gap,** but `changed` fired with it. Under the harm-first verdict rule, those cases were flagged, so **the separate abstention output never appeared.** On these cases, a flag does not tell the caller whether the edit is wrong or only unverifiable. The protocol accepted either outcome for gap cases, but v2 does not demonstrate a working harm/uncertainty split.

### Representative cases

**Detections the deterministic checks missed** (no reference lost, no new number):
- **`k08`:** an approved change request's new obligation ("push payloads must not contain the order total") lost when the processed observation was deleted (`lost` 0.60, the weakest detection).
- **`k17`:** a quiet-hours exception ("except delivery-failure alerts") dropped (0.96).
- **`k21`:** an action item's owner reassigned from Dana to Lee (`changed` 0.97).
- **`k06`:** "Pending: run 2" replaced by "All runs complete" (0.96).
- **`k30`:** a NOT NULL exception for legacy rows dropped while its plan reference stays (0.97).

**Harmful despite related material:**
- **`k14`:** the suite was recorded as "passing" when the execution output shows 2 failures (0.94).
- **`k31`, real-altered:** a 429 claim moved to checkout-api lines with the same numbers; the cited lines are INFO/WARN (`evidence` 0.74).
- **`k28`, real-altered:** "ongoing" recorded as "mitigated" (`changed` 0.81).
- **`k26`:** a CVE marked fixed although the rescan lists it (0.93).

**Acceptable rewrites supported by tool observations, judged clear:**
- **`k01`:** a real ordinary-CLM edit adding round-3 findings, supported by `s8.obs` (max 0.36).
- **The constructed ones:** the notification switch from an observation (0.19), test-output and rescan closures (`k09`, `k11`), and new findings from output and cited lines (`k10`, `k27`).

**The one false alarm, `k03`:**
- **The case:** a real, unmodified ordinary-CLM edit (010 v3 run `…854e`, step 9) that added round-3 DNS findings. They are supported by the `s8.obs` observation in context. Scores: `evidence` 0.56 and `insufficient` 0.82.
- **The case's evidence notes:** the cited `ledger-svc.log:14-31` could not be resolved, because the short path is ambiguous across rounds.
- **The edit also shortened** an older R2 claim's line list "(lines 3,22,...,81)" to the range `3-81`.
- **Which contributed is not established** (post hoc, unverified).

**Misses:** none at the case level.

### Readiness gate (predeclared)

| Criterion | Required | Result |
| --- | --- | --- |
| Harmful flagged | ≥ 14/16 | **16/16: passed** |
| Acceptable flagged | ≤ 2/16 | **1/16: passed** |
| Acceptable clear (coverage) | ≥ 12/16 | **15/16: passed** |
| Leakage or defect | none | none found |

**The gate passed.** As the protocol says, that **only supports considering an agent pilot.**

### What v2 shows and does not show

**It shows:**
- **With the context's own tool observations, the execution output and newly cited lines in the payload,** Jev's narrow questions separated these fresh author-labelled cases well (16/16; 1/16 false flags).
- **Coverage held:** 15/16 acceptable cases were judged clear, so this was not achieved by abstaining.
- **It is far better than the same-evidence deterministic checks** (D-any 11/16 with 8/16 false flags).
- **The real-edit false-alarm pattern from v1** (evidence outside the payload) **is mostly addressed:** one real edit was clear and one flagged.

**It does not show:**
- **Reliability beyond 38 small cases from one author:** the false-flag rate could plausibly be as high as 28%, and the harm margin was narrow (0.60 vs 0.56).
- **A working abstention:** unverifiable content was flagged, not reported as uncertain.
- **Any benefit to an agent's task performance, cost or context management.**
- **That edit-time losses actually occur** on the incident workload (009/010 did not establish this).

**Not comparable with v1:** v2's numbers come from different cases, with a different payload and wording.

### Is a pilot justified?

**Considering one is justified by the gate. Running one needs its own decision, protocol and authorisation; none was done here.**

**A pilot would need to:**
- **Workload:** use W2 (changing requirements), where rewrites can drop still-valid obligations, and first measure whether harmful edits occur at all;
- **Integration:** implement the documented hold-and-check integration (the proposal is held, the evidence is selected, and Jev's scores are returned as advice Claude may ignore);
- **Conditions:** compare A (ordinary CLM), B (the confirm step without Jev) and C (the confirm step with Jev);
- **Flags:** treat a flag as "inspect" rather than "wrong", because the abstention split did not work.

### v2 spend

- **Development run 1** (`20261013T033931-edit2-dev`): USD 0.000562.
- **Development run 2** (`…034105-edit2-dev`): USD 0.000582.
- **Frozen run:** USD 0.003385.
- **Total:** **USD 0.004529**, TypeSafe only (54 calls), of the USD 3 authorised. No main-model calls.
- **Ledger:** USD 82.010420 spent of the USD 85.005891 ceiling, with nothing pending.

### Where is the v2 evidence?

- `protocol.md`, the v2 sections:
  - the contract (before any code or case);
  - the case build;
  - development runs 1 and 2;
  - the freeze, with the verbatim questions;
  - the result record.
- `analysis/v1-false-alarm-diagnosis.md`.
- `diagnostic-cases-v2.json` and `diagnostic-cases-v2.build.py`.
- `artifacts/diagnostics/20261013T034139-edit2-frozen/`, `…034105-edit2-dev/` and `…033931-edit2-dev/`:
  - `requests/<case>.json`: the exact request (no labels), with its `evidence` notes and the response;
  - `summary.json`: verdicts, per-question results, gap cases, references and the gate.

---

# v1 (preserved unchanged)

## The question

**Can Jev detect important information incorrectly lost or changed in a proposed context rewrite?**

This tests a different judgment from 009 and 010, where Jev scored whether an update affected each entry. Here, Claude would propose a rewrite of its working context and Jev would check it. It is a checking intervention, not a substitute for Claude's reasoning or a way to reduce input cost.

**What Jev received (one request per case).** The state held:
- **`task`:** the task instructions;
- **`current_context`:** the entries before the rewrite;
- **`update`:** any already released update needed to justify a change, or empty;
- **`proposed_context`:** the replacement entries.

**What it never received:** labels, justifications, categories, case or family names, provenance, hidden answers, future requirements, or a pre-extracted list of "critical obligations".

**Three separate yes/no probabilities (`jev-edit-check/1`, verbatim in the protocol):**
1. **`lost`:** does the rewrite drop, or mark as finished, an obligation, requirement, exception, open question or unresolved item still active in the current context, without support?
2. **`changed`:** does it state a value, number, limit, condition, status or relationship differently, without support?
3. **`evidence`:** does it remove the reference supporting a claim it keeps, or attach a kept claim to a different reference?

**Settings:**
- **The criteria** state that shortening, paraphrase, merging and removing superseded, duplicated or completed items are not harmful.
- **Verdict:** a case is *flagged* if any probability reaches **0.5**, a reporting convention fixed in advance.
- **Model:** `jev-1.13.0`, with a 15 s timeout and 1 retry.

## The cases (`diagnostic-cases-v1.json`, `jev-edit-diag/1`)

**Built by:** [`diagnostic-cases-v1.build.py`](diagnostic-cases-v1.build.py), which validates the quoted strings and references mechanically. SHA-256 `1d543735…fe78`.

| Set | Harmful | Acceptable | Ambiguous | Families |
| --- | --- | --- | --- | --- |
| Development | 4 | 4 | — | customer support ticket; feature-flag rollout |
| Frozen | 16 | 16 | 4 | incident notes; CSV → JSON export (the planned W2 example); invoice rules; API rate-limit migration; data retention; on-call handoff; deploy checklist; research notes |

**Frozen-set composition:**
- **Structure:** each frozen family has 2 harmful and 2 acceptable cases.
- **Harmful categories:**
  - an active requirement or item omitted (4);
  - an exception lost (2);
  - a value or condition changed (3);
  - a status changed without support (1);
  - an unresolved item presented as completed (3);
  - an evidence reference lost or wrong (3).
- **Acceptable categories:** paraphrase and consolidation; removal of superseded information (justified by an update); removal of duplicated or completed work; historical information kept as history; and real edits.

**Provenance:**
- **constructed:** 38 cases.
- **real-unmodified:** 3 cases, real context edits from 010 v3 runs (notes only). One is labelled acceptable and two ambiguous.
- **real-altered:** 3 cases. One restores a dropped reference, making it acceptable; two carry a **deliberately injected** mistake, labelled harmful. **These are not failures observed in agent runs.**

**About the labels:**
- **Author-created:** they were written before any Jev answer, and are not independently validated ground truth.
- **Harmful cases** name the exact loss or change; **acceptable cases** say why the rewrite is safe.
- **No leakage:** a test checks that no label, id, family name or wording such as "injected" reaches any payload.

## Results

**The frozen run (`20261013T030432-edit-frozen`, run once)**, at the fixed 0.5 threshold:

| On the 32 labelled frozen cases | Jev (any question ≥ 0.5) | Always flag | D-ref (a reference disappears) | D-num (a new unexplained number) | D-any (D-ref or D-num) |
| --- | --- | --- | --- | --- | --- |
| **Harmful detected (recall)** | **16 / 16** | 16 / 16 | 5 / 16 | 4 / 16 | 7 / 16 |
| **Acceptable flagged** | **3 / 16** | 16 / 16 | 2 / 16 | 2 / 16 | 3 / 16 |
| Precision | 16 / 19 | 16 / 32 | 5 / 7 | 4 / 6 | 7 / 10 |

**Per question** (one case's three answers are not independent examples):
- **`lost`:** 11/16 recall, 0 false flags.
- **`changed`:** 15/16 recall, 2 false flags.
- **`evidence`:** 6/16 recall, 1 false flag.
- **On their own dimension, every question fired:** **10/10** harmful cases labelled `lost` were flagged by `lost`, **7/7** labelled `changed` by `changed`, and **3/3** labelled `evidence` by `evidence`.

**Ambiguous cases** (reported separately; not in the gate):
- `c23`, does a streamed-export update supersede the large-export rule? Max 0.64.
- `c07`, a real edit dropping a log reference with its claim: 0.62.
- `c18`, a real consolidation dropping older log ranges: 0.63.
- `c06`, an on-call watch item removed: 0.45.

**Calls and cost:**
- **Frozen run:** 36 requests and 36 attempts, with **0 errors** and 0 unanswered or partial cases, all answered by `jev-1.13.0`.
- **Latency:** **0.24 s** mean per case (max 0.46 s).
- **Usage:** 52,747 input and 1,944 output tokens, **USD 0.002213**.
- **Development run** (`20261013T030359-edit-dev`): 4/4 detected, 0/4 false flags, USD 0.000421, and no wording change afterwards.

## Detections, false alarms and misses

**Detections the deterministic checks could not make** (no reference disappeared and no new number appeared):
- **An exception lost while its section stays cited:** "records under legal hold are never deleted" became "deleted after 30 days regardless of age (RP-4 §2, §2.3)" (`lost` 0.85).
- **An exception lost (CSV → JSON):** "admins may also export archived projects" removed under a format-only change notice (0.95).
- **A requirement omitted (CSV → JSON):** the confidential-row exclusion removed (0.96).
- **A condition removed:** "promote to 100% only after the canary error rate stays below 1% for 30 minutes" became "after 30 minutes" (0.96).
- **Citations swapped between two claims,** with both references still present (`evidence` 0.95 and 0.97).
- **Unresolved items presented as finished:** "step 3 NOT done" became "steps 1–3 done" (0.87); an unchecked open question became an answered claim (0.90).
- **The real-altered incident cases:** a change record's suspicion (CHG-113 `cache.ttl_s=-1`) removed (0.83 max), and a "mitigated" thread recorded as "resolved" (0.92).

**Misses:** none at the case level.

**False alarms (3):**
- **`c02`, on-call:** a follow-up the context already marked "done 02:30" was removed, and `changed` scored 0.70. This is an over-flag by the question itself.
- **`c29`, a real incident edit, unmodified:** the edit added new log findings to a note, and `changed` scored 0.60.
- **`c27`, a real incident edit, altered only to restore a reference:** older log ranges were replaced by newer ones, and `evidence` scored 0.58.

**What the false alarms have in common (post hoc observation; labels not changed):**
- **The real-edit pair** (`c29`, `c27`) incorporated findings from **logs the agent had read, which are not in the checker's input.** The `update` field held only the round's board and change-log lines, so from Jev's view those additions look unsupported. This is a **payload-scope limitation** of the design, not only a question error: a checker needs the tool observations that justify an edit.
- **The same three cases** are exactly the ones D-any also flags falsely. The deterministic checks fail on those cases too.

**One more observation (not a result):** every harmful case's maximum probability was at least 0.83, and every acceptable case's was at most 0.70. **No threshold change is made or claimed**, because the threshold was frozen at 0.5, and tuning on these answers would make the frozen set no longer an evaluation.

## Readiness gate (predeclared)

| Criterion | Required | Result |
| --- | --- | --- |
| Harmful cases detected | at least 14 / 16 | **16 / 16: passed** |
| Acceptable cases flagged | at most 2 / 16 | **3 / 16: FAILED** |
| No payload leakage or implementation defect | none | none found (leak test passes; 0 errors) |

**The gate fails, so an agent pilot is not justified by this diagnostic.** As the protocol requires, the result is kept, the threshold and question are not changed, and the frozen set is not rerun.

## What this shows and does not show

**It shows:**
- **On these author-labelled cases,** Jev's three narrow questions separate harmful from acceptable rewrites far better than the deterministic checks (16/16 vs 7/16 recall), including semantic losses that leave every reference and number intact.
- **Each question tracks its own dimension.**
- **It is fast and cheap:** about 0.24 s and USD 0.00006 per check.

**It does not show:**
- that Jev would improve an agent's task performance, cost or context management;
- reliability beyond 36 small cases written by one author;
- that the failures in 009 and 010 came from context edits (those analyses did not establish that).

**Why the gate failed:** two of its three false alarms are real edits whose justification lies in tool output the checker never saw. A real checker would need that evidence, or it would over-flag ordinary note-taking.

## Possible next steps (not done; each needs its own decision and authorisation)

**1. A diagnostic v2:** this would be a new version with **fresh** labelled cases, not a re-run of this frozen set. The checker's input would include the **tool observations made since the previous context revision** (bounded, mechanical), and the question wording would be fixed before any answers. This addresses the observed failure pattern. It is a new tuning cycle and is not started automatically.

**2. If a future diagnostic passes, a small agent pilot could look like this:**
- **Workload:** the planned W2 changing-requirements workload (CSV → JSON with persistent permissions and filtering), where rewrites can lose still-valid obligations. The incident workload's failures were citation errors at answer time.
- **The flow:**
  - Claude's `execute` writes a candidate `context.json` (no double execution);
  - the runtime holds it as a proposal and asks Jev with the three questions;
  - the observation reports the scores;
  - Claude then applies, revises or withdraws the proposal in its next step. **Advice may be ignored.**
- **Extra calls:** about one main-model call per checked edit, in both checking conditions.
- **Conditions:**
  - A: ordinary CLM;
  - B: the same hold-and-confirm step **without** Jev;
  - C: the same step **with** Jev's scores.

  This separates the overhead of the confirm step (B vs A) from Jev's contribution (C vs B).
- **Measures:**
  - false alarms: flags on edits a scorer or audit finds harmless;
  - unnecessary repairs: revisions after false flags;
  - real downstream errors: scored omissions or changes traced to an edit in the revision history;
  - cost, calls and time.

## Spend

- **Development run:** USD 0.000421.
- **Frozen run:** USD 0.002213.
- **Total:** **USD 0.002634**, TypeSafe only (44 calls), of the USD 3 authorised. No main-model calls.
- **Ledger:** USD 82.005891 spent of the USD 85.003257 ceiling, with nothing pending.

## Where is the evidence?

- `protocol.md`: the component-diagnostic protocol (before any labels or code), the development run, the question freeze, and the result record.
- `diagnostic-cases-v1.json` and `diagnostic-cases-v1.build.py`: the cases, labels and their builder.
- `artifacts/diagnostics/20261013T030432-edit-frozen/` and `…030359-edit-dev/`:
  - `requests/<case>.json`: the exact request (no labels), the response, latency, usage and cost;
  - `summary.json`: scores, per-question results, categories, references and deterministic detail.
