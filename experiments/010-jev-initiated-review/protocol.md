# 010 – Planned protocol: Claude-initiated review with Jev assistance (strategy 2)

**Status: PLANNED. Not implemented, not run, and no paid calls are authorised.** Written on 2026-10-13 as part of the [roadmap](../jev-assistance-roadmap.md). Any implementation would first freeze a revised version of this protocol.

## Question

**When Claude itself decides that its context needs review, does consulting Jev as part of that review improve it?**

## Design

**Both arms get the same, versioned `review` action.** Its use is Claude's choice in both arms, and the runtime never forces it.
- **The request:** Claude names an update, either as text or as the id of a current entry, and the current entries it wants reviewed.
- **The runtime returns:** the named entries' exact text from the **current** revision (008's boundary rule), as a structured review prompt.
- **The next step:** Claude decides whether and how to edit.

**The arms:**
- **A (control):** the review action returns the structured review prompt only. Claude performs the review itself.
- **B (assisted):** the same action also returns Jev's per-entry `jev-review/1` probabilities for the named entries, against the named update.

**How this differs from 008:** in 008 the control had **no** review mechanism, and B's Jev action was an independently optional extra, which the agent never used. Here the review mechanism and its wording are identical in both arms, so how often reviews happen can be compared directly. Advice is the only difference.

| | |
| --- | --- |
| **Jev judgment** | The same as 008 and 009: whether the update requires reconsidering a current assertion or planned action in each named entry |
| **Trigger** | Claude's own decision, at most N per run (for example 12) |
| **Information: Claude** | Its own context; the review prompt (both arms); the advice (B) |
| **Information: Jev** | The update Claude named, and the named current entries only |
| **Who edits** | Claude, in a later step, through the normal validated edit path |
| **Overhead** | Each review is one extra Claude turn in **both** arms, plus a Jev round trip in B |

## Possible failure modes

- **Reviews are rarely or never initiated**, as 008 found for an optional tool. This is the first thing to measure, and no prompt strengthening is allowed after results.
- **Paraphrased updates:** Claude-named update texts may be paraphrases. The update text then is not the original evidence, unlike 009's payload.
- **Selective review:** Claude may name only entries it already intends to change, which makes the advice redundant.
- **Bias toward agreeing with the advice.**
- **Overhead** from extra turns, in both arms.

## Diagnostics before any evaluation

- **Jev side:** 009's `jev-diag/2` results cover the question on real payloads. A small check is still needed of whether the update texts Claude writes in the pilot look like the payloads Jev was checked on. Those texts would be labelled after the pilot, so they are development evidence only.
- **Logging:** review frequency, timing (steps after a release) and the scope chosen.

## Outcomes

- **Primary:**
  - the number of reviews initiated per run in each arm;
  - strict success;
  - all-attempt cost.
- **Secondary:**
  - edits following reviews;
  - flagged-then-changed and flagged-not-changed;
  - calls, time and cache use.

## Limitations

- **Arms with different numbers of reviews are not matched on review count.** Differences are reported per run rather than adjusted.
- **Scope:** the same synthetic task family and model as 009.

---

## Finalised protocol (2026-10-13, session 5, before any code or paid 010 call)

_This supersedes the planned design above where they differ. The plan is kept as written._

### Question

**When Claude initiates a review of its working context, does Jev's advice improve the resulting agent performance?**

**How this differs from earlier experiments:**
- **Not 008:** there, Claude had to choose to call an optional Jev tool, and never did. Here Claude chooses to **review**, and in the assisted condition every review automatically includes Jev.
- **Not 009:** there, a review happened at every incoming update. Here reviews happen only when Claude starts one.

### Mechanism (`initiated-review/1`), identical in both conditions

**How Claude initiates a review:** a new action, available in both conditions, `{"action": "begin_review", "new_information": "<text>"}`, with an optional `thought`.
- **What Claude supplies:** `new_information`, the information that Claude judges may have made parts of its context out of date (quoted or summarised, 1–2,000 characters).
- **What it does not supply:** entry ids, revisions or proposed edits. The trigger expresses a *need* to review, not a decided edit.

**What happens, in the same step, with no extra model call:**
- **Candidates:** the runtime takes the **current** context revision R (the one shown in that step's request) and selects the candidate entries by a **structural rule**:
  - **included:** entries with role `note`, `observation` or `summary`;
  - **excluded:** step actions (`assistant`) and runtime edit receipts (`receipt`);
  - **cap:** at most 60 scored, with any beyond listed as not assessed.
  - **Difference from 009:** 009 scored every entry, and about a third of its flags fell on step-action code entries. This exclusion is a design choice, **not** a proven improvement.
- **Control (A) receives** an observation: `Context review (initiated-review/1; context revision R). New information (as you stated it): <text>.`, the candidate ids (and any excluded runtime entries, as a count), and: "Review these entries against the new information and decide in your next step whether and how to edit context.json; you may also leave it unchanged. Your context is unchanged."
- **Assisted (B) receives** the same observation, plus Jev's advice block (the 008/009 format):
  - the fixed question `jev-review/1`, with `state.update` = the new information;
  - every candidate's probability, or "no answer";
  - coverage, and any service problem.

  The advice is computed on the host **before** that observation is returned, so it is in Claude's next request, before any associated edit.

**Who edits:** Claude, in later steps, through the normal validated `execute` path. There is no automatic deletion, no mandatory acceptance and no probability-to-edit rule.

**Editing without a review remains possible** at any time, in both conditions.

**Main-model turns:**
- **A review:** one turn (`begin_review`), then at least one more turn to act on it.
- **A direct edit:** one turn.

Both are the same in both conditions. No dummy calls, sleeps or padding.

**Tie to the revision:** advice is always computed for the revision current at the review step, and labelled with it. A review cannot name an older revision, which removes the 008 failure class: deleted entries are never sent.
- **After an edit,** advice still visible in Claude's context refers to revision R by label. A later review always uses the then-current revision.
- **Recorded per review:** R, the candidate ids, the excluded ids, the answers, and the accepted edits until the next review (by revision and entry id).

**Limits and failures:**
- at most **12 reviews per run**;
- an empty, over-long or over-limit request is rejected with a notice, at no Jev cost, in both conditions;
- Jev: a 15 s timeout and 1 retry (429/529/5xx/timeouts). A failure gives "no answer" plus a service notice, and the run continues.
- Every attempt is a ledger entry (kind `jev`).

**Release observations:** the historical text (no 009 update payload). Claude reads the round files itself, as in 007 and 008.

### Prompts (new version; earlier texts unchanged)

**Both conditions** (`INITIATED_REVIEW_CLAUSE`):

```
CONTEXT REVIEW (this run):
- When you judge that new information may have made parts of your working context out of date,
  you can start a context review: reply {"action": "begin_review", "new_information": "<the new
  information, quoted or summarised>"}. Routine edits (for example removing step entries you no
  longer need) do not need a review.
- The runtime replies with the context revision and the entries to review (your notes and
  observations). In your next step, decide whether and how to edit context.json; you may also
  leave it unchanged. A review uses one model call. You can edit context.json at any time without
  a review.
```

**Assisted only** (`INITIATED_REVIEW_JEV_CLAUSE`):

```
- In this run, each review also asks a fast classifier (Jev), for each listed entry, for the
  probability that the new information requires reconsidering a current assertion or planned
  action in it. The advice is probabilistic and can be wrong, and it never edits your context. A
  low probability is not a reason to delete an entry, and a high one does not mean the entry is
  wrong. You decide whether and how to edit.
```

**The control is "CLM with the initiated-review protocol"**, not 007's, 008's or 009's control. The review action and its instruction may change ordinary CLM behaviour.

### Shared settings

**Config:** `configs/exp010.toml`, which is `configs/exp009.toml` with update review **off**, `[initiated_review]` added, and the 010 ceiling.

**Identical in both conditions:**
- `claude-opus-5-5`, effort low;
- an 8,000-token request budget, 4,096 output tokens and 60 task calls;
- mode `clm_helpers` (reusable helpers allowed);
- the same fixtures, released evidence, file access and tools;
- the `blocks/1` layout, 5-minute prompt caching on, and `run-tag/1` cold isolation per run;
- the spill and pressure fixes, and the revision status line;
- the scorer `rounds-score/1` and the failure rules.

**Conditions:** A `clm_helpers+rev:on`, B `clm_helpers+rev-jev:on`.

### Calibration (4 runs) and readiness gate

**Runs:** `rounds-dev-1`, `rounds-dev-2` (development instances, already used by 007–009) × A, B, in the order dev-1 A, B; dev-2 B, A. That is exactly four runs. A separately labelled forced-use plumbing diagnostic is allowed only if the calibration leaves the live path unverified, and is excluded from comparisons.

**The gate passes only if all of these hold:**
1. **Reviews are used by both arms.** Each condition initiates at least one review in at least one of its runs, and the two arms together initiate at least 4 reviews.
2. **Reviews come while work remains.** At least one review in each condition comes before the last round is released.
3. **The assisted path works live.** Real Jev calls occur at B's reviews, the advice appears in the next request before any associated edit, and candidates are non-empty current-revision entries.
4. **The machinery works:** context edits still govern later requests, and accounting (both providers), caching, scoring and export work.
5. **No material implementation defect.**
6. **The projected evaluation fits:** mean calibration cost per run, per arm, × 12 × 1.25 fits the remaining authorisation.

**Not required:** that Jev improve scores, cost or speed, that correctness be imperfect, or that Claude agree with Jev.

**If (1) or (2) fails:** preserve the runs, stop with a diagnosis, and do **not** strengthen the instructions.

### Evaluation (only if the gate passes)

**Sample:** 4 fresh instances `rounds-eval-9..12` (seeds 7209–7212), registered after calibration and validated mechanically only, × 3 repetitions × 2 conditions = **24 runs**.

**Order:** alternating by instance index + repetition (as 009). Settings, the code patch and the full schedule are frozen before the first evaluation call.

**Failure rules:**
- every run is kept, and none is replaced or repeated;
- `compare` halt statuses halt the evaluation;
- a material defect stops it and is documented, and results from before and after a fix are never pooled;
- no tuning, and no stopping on results.

### Metrics

- **Correctness:**
  - strict success, and checks by category (causes, services, status, evidence, unresolved);
  - stale facts, missing causes and invalid citations.
- **Cost and time:**
  - mean and median cost, including Jev;
  - elapsed, Anthropic and Jev time.
- **Activity:**
  - main-model calls, reviews (accepted and rejected), executions and accepted edits;
  - tokens and cache reads and writes.
- **Advice:**
  - advice characters;
  - advice **residence**: the number of later requests that still carried each review observation.
- **Failures:** retries, recoveries and repairs.
- **Review-to-edit links:** candidates changed after a review, flagged or unflagged then changed, and flagged but not changed. These are temporal association only.
- **Exploratory:** whether each scored omission was information lost in a context edit or present in context but omitted from the answer. The scorer is unchanged.
- **Structure of the analysis:** matched blocks and per-instance aggregates, with repeated runs distinguished from independent instances.

### Budget

- **Authorised:** up to **USD 30 of additional total spend** for 010 (both providers, calibration, diagnostics, retries and evaluation). It replaces unused earlier allowances.
- **The ceiling** is set explicitly to the settled spend at the start + 30.
- **After calibration:** if the projected evaluation does not fit, stop and report, without shrinking the evaluation.

## Session record (2026-10-13, session 5)

1. **Before any paid call:** the roadmap was revised, the protocol above was finalised, and the implementation was built.
   - **Checks:** 181 tests passed (10 new in `tests/test_initiated_review.py`); ruff, format and mypy clean.
   - **Budget:** ceiling set from USD 70.210028 to USD 89.687573 (settled spend USD 59.687573 + 30, with nothing pending).
2. **Calibration:** comparison `20261012T204507`, 4/4 runs, in the frozen order. The prompt text matches this protocol verbatim.
3. **Gate outcome: FAILED.**
   - **Criteria (1) and (2) failed:** **zero** `begin_review` actions in all four runs, in both conditions.
   - **The mechanism was exposed:** the clause, the schema enum and the status line appeared in every request.
   - **The runs are kept.** The instructions were not changed, no forced-use substitute was run, and the evaluation was not started.
4. **No forced-use plumbing diagnostic was run.** It is not needed for any comparison, because the evaluation is not running. The new action's Jev path shares the scoring code that 009 exercised live.
5. **Spend:** USD 1.521721 (Anthropic only). The ledger is at USD 61.209294 of USD 89.687573.

---

# Protocol v2: required pre-edit review (2026-10-13, session 6, written before any v2 code or paid call)

_Protocol v1 (the finalised protocol and session record above) and its calibration (comparison `20261012T204507`) are preserved unchanged. **v1 finding:** when review was optional, Claude bypassed it and edited directly in all four runs. v2 is a separately versioned design within experiment 010. Its runs carry the phases `v2-calibration` and `v2-evaluation`, are exported under `artifacts/runs/v2/…`, and are never pooled with v1._

## Question

**When Claude decides to edit its working context, does a Jev-assisted review improve the outcome enough to justify its overhead?**

This is not a test of voluntary Jev adoption. How it relates to the neighbouring experiments:
- **009:** review triggered by incoming evidence.
- **010 v2:** review triggered by Claude's own decision to edit its context.
- **011 (planned):** evaluates the *content* of a proposed replacement. Not implemented here.

## Conditions and predeclared contrasts

| | Condition | Workflow |
| --- | --- | --- |
| **A** | Ordinary CLM (`clm_helpers:on`) | The existing direct-editing workflow: no review action, no requirement, no Jev |
| **B** | CLM with a required pre-edit review, no Jev (`clm_helpers+pre:on`) | Before any `context.json` edit, Claude starts a review, receives the review material, then chooses its edit in a later step |
| **C** | The same required review, with Jev (`clm_helpers+pre-jev:on`) | Identical to B, plus Jev's advisory scores in the review material for update reviews |

**Contrasts:**
- **C vs A:** the practical end-to-end effect of deploying the Jev-assisted workflow.
- **C vs B:** the incremental effect of Jev within the shared review workflow.
- **B vs A:** the effect and overhead of the review workflow itself.

Savings measured against B alone are **not** savings against ordinary CLM. A receives no dummy calls or delays.

## Mechanism (`initiated-review/2`), identical in B and C

**Review action:** `{"action": "begin_review", "purpose": "update", "new_information": "<text>"}`, or `{"action": "begin_review", "purpose": "compaction"}` when Claude only wants to compact or reorganise and no factual update is involved.
- **`thought`** is optional.
- **No draft:** no replacement draft or entry list is required.
- **Validation:**
  - `update` needs 1–2,000 characters of new information;
  - `compaction` must not carry any.

  An invalid request is rejected with a notice. It authorises nothing and makes no Jev call.

**Review material (same step, no extra model call):**
- **Contents:** the current revision R, the purpose and the stated information. It also lists the candidate entry ids under the v1 structural rule: roles `note`, `observation` and `summary`, with step actions and receipts excluded, at most 60.
- **Nothing duplicated:** entry bodies are already in Claude's context and are not repeated.
- **The instruction:** decide in a later step whether and how to edit; not editing is allowed.
- **C, update reviews only:** Jev's advice block, computed on the host before the observation is returned, so it reaches Claude's next request before any edit. Advice is never returned after an edit.

**Authorisation:** a valid review issues **one** edit authorisation, bound to the reviewed content: the bodies of every entry of R.

- **When an edit is accepted:** `context.json` must change content in a later step's `execute`, and pass the existing validation. The authorisation must be present, and every entry of R must still be present with an unchanged body in the current revision.
- **What does not invalidate it:** runtime appends of action, observation and receipt entries in later steps add entries without changing R's entries.
- **How it ends:**
  - **consumed** by the first accepted, content-changing edit;
  - **replaced** by a new valid review;
  - **expired** when the next round is released (`advance`), so a review covers only the evidence available when it was made;
  - **invalidated** if any of R's entries changed, which only a runtime spill can do in practice;
  - **unused** at the end of the run.
- **Steps between review and edit:** steps that read files or write other files leave the authorisation intact.

**Without a valid authorisation:** a content-changing write to `context.json` is **rejected** through the existing rejection path.
- **What is kept:** the previous context, and the rejected bytes are saved to the trace.
- **The receipt says why:** "edit rejected: context edits in this run require a review first …".
- **What it does not count as:** an accepted edit.
- **What is not undone:** other side effects of that code (printed output, other files). There is no rollback.
- **Rewrites that don't change content:** they remain "unchanged writes", are not edits, and need no authorisation.
- **No double execution:** model code is executed once; there is no dry run.

**Runtime appends are not model edits.** They never need, consume or trigger a review, so there is no recursion.

**Status line (B and C):** `context edit authorisation: none (start begin_review before editing context.json)`, or `available from the review at step s (revision R)`. Both conditions also show the existing "context revision N" and "context reviews used k/40".

**Main-model turns:** every accepted edit needs at least two turns in B and C (a review, then an edit), against one in A. This overhead is real and is charged.

## Jev's job (C only), kept narrow

- **Question:** `jev-review/1`, unchanged: does this update require reconsidering a current assertion or planned action in this entry? The update is Claude's stated `new_information` for an `update` review.
- **Candidates:** the structural rule above, applied to the current revision.
- **Pure compaction:** with no factual update, the question does not apply. The review records **not applicable**, no Jev call is made, and the material says "Context review advice: not applicable (compaction review: no new information stated)". Such reviews do not demonstrate Jev assistance and are counted separately.
- **Not other judgments:** Jev does not judge the replacement draft, current relevance, or safety to delete. "Affected by the new information" is not treated as "delete" or "keep".
- **Advice format:** the 008/009 block (probability per candidate, coverage, any service problem).
- **Lifecycle:** the advice lives in the review observation, which Claude may delete, and its residence is measured.
- **Service errors:** "no answer" plus a notice. The review still authorises the edit, and the run continues. There is one retry, every attempt is in the ledger, and nothing is automatic: there is no threshold rule and no forced acceptance.
- **Jev sees** only the stated new information and current-revision entry bodies. It never sees deleted revisions, future rounds, truth, scorer data or credentials.

## Shared settings and limits

- **Config:** `configs/exp010v2.toml`, which is `configs/exp010.toml` (the 009 and 010 runtime) with three changes, applied **equally to A, B and C**:
  - **`max_calls` raised from 60 to 90:** v1 and 009 runs used 30–36 calls and made 11–23 edits, and B and C need about one extra call per edit;
  - **`[initiated_review] max_reviews` set to 40;**
  - **the v2 ceiling.**
- **Unchanged:**
  - the model `claude-opus-5-5` (effort low), an 8,000-token request budget and 4,096 output tokens;
  - mode `clm_helpers`, the historical release text, and the same fixtures, files and tools;
  - the `blocks/1` layout, 5-minute caching and `run-tag/1` cold isolation;
  - the spill and pressure fixes, the revision status line, and the scorer `rounds-score/1`.
- **Unavoidable differences:** A has no review action, no status line about authorisation, and no extra clause. That difference is the intervention under test.
- **Not direct controls:** 009's and v1's runs are separate, and are not controls for v2.

**Prompts (new version):** B and C get `INITIATED_REVIEW_V2_CLAUSE`, and C also gets `INITIATED_REVIEW_V2_JEV_CLAUSE`. The texts are in the session record below, and the code is checked against them.

## Offline verification before paid work

**Focused tests:**
- B and C cannot bypass the review;
- A keeps direct editing;
- the review precedes the edit decision;
- revision binding, runtime appends, one-use consumption and expiry;
- advice never edits;
- no-op, rejection, compaction and service-error paths;
- no hidden information reaching Jev;
- cost and evidence records;
- the separated v1/v2 export paths;
- historical compatibility.

**Plumbing checks:** one **scripted-provider** run with the real Jev service (TypeSafe only), labelled `plumbing`, if the live path needs verification. It is excluded from all results.

## Calibration (6 runs) and gate

**Runs:** `rounds-dev-1` and `rounds-dev-2` (development instances) × A, B, C, using the three-condition rotation (block 0: A, B, C; block 1: B, C, A). Exactly six runs.

**The gate passes only if:**
1. **The workflow is used:** B and C actually use the review-before-edit workflow. Each has accepted edits authorised by reviews, and no accepted edit lacks one.
2. **Jev reviews happen:** C makes at least 2 **applicable** (update) Jev reviews before the last round is released, across its runs.
3. **Advice comes first:** advice is in the request before every subsequent accepted edit in C.
4. **No defect:** no bypass, revision-binding or accounting defect.
5. **The machinery works:** accounting (both providers), caching, scoring and export all work.
6. **The projected evaluation fits:** the mean calibration cost per run per condition × 12 × 1.25, summed over conditions, fits the remaining authorisation.

**Not required:** better results with Jev, agreement with Jev, or imperfect control accuracy.

**If the gate fails:** preserve the runs and stop. Prompts are not strengthened, and development runs are not repeated.

## Evaluation (only if the gate passes)

**Sample:** 4 fresh instances `rounds-eval-9..12` (seeds 7209–7212) × 3 repetitions × 3 conditions = **36 runs**.
- **The instances** were reserved by v1 and never registered or used. They are checked again for prior use, then registered and validated mechanically only.

**Schedule:** 12 blocks (repetitions outer, instances inner). Block b uses order b mod 6 of the six permutations of (A, B, C), so each condition takes each position 4 times. It is frozen, with settings and a source patch, before the first evaluation call.

**Failure rules (as before):**
- every run is kept;
- nothing is replaced or repeated;
- `compare` halt statuses halt the evaluation;
- a material behavioural defect stops it and is documented, and results from before and after a fix are never pooled;
- no tuning, and no stopping on results.

## Metrics

**Per condition:**
- **Correctness:**
  - strict success and checks by category;
  - stale facts, missing incidents and invalid citations.
- **Cost and time:**
  - mean and median total cost (including Jev);
  - elapsed, Anthropic and Jev time.
- **Activity:**
  - main-model calls;
  - reviews by purpose;
  - accepted edits;
  - edits blocked for lacking a review;
  - authorisation outcomes (consumed, expired, replaced, invalidated, unused).
- **Jev:** applicable and not-applicable reviews, coverage, errors, tokens, cost and latency.
- **Tokens:** cache reads and writes, input and output tokens.
- **Advice:** advice characters and residence.
- **Failures:** retries, repairs and recoveries.

**Comparisons:**
- all three contrasts, by matched block and per instance;
- four instances × three repetitions are repeated measurements of four tasks.

**Traces:**
- edit initiation → review material and advice → the actual edit or no edit;
- advice ignored, misleading or redundant.

Advice preceding an edit is not evidence that the advice caused it.

## Budget and stopping

- **Authorised:** up to **USD 30 of additional total spend** for v2 (both providers, verification, calibration, retries and evaluation). It replaces earlier unused allowances.
- **The ceiling** is set to the settled spend at the start + 30, with `configs/exp010v2.toml` matching.
- **Live commands:** sequential only.
- **After calibration:** if the projected 36-run evaluation does not fit the remaining authorisation, stop and report. The evaluation is not shrunk.

## v2 session record: before any paid call (2026-10-13, session 6)

- **Implementation (clm-lib, opt-in):**
  - **The gate:** `ContextStore.read_back(..., authorise=...)` is asked about a valid, content-changing candidate before commit. A refusal reuses the existing rejection path.
  - **The review step:** `_Run._begin_review_v2` handles a review and issues the authorisation.
  - **The checks:** `_authorise_edit` (binding, invalidation, recovery exemption), `_settle_edit_auth` (consumption, blocked edits) and `_end_edit_auth` (outcomes).
  - **Expiry:** at `advance`.
  - **The conditions:** `+pre` and `+pre-jev`, with run ids `-pre` and `-prejev`.
  - **Exports:** `ir_*` v2 columns, and an optional export `group`, so v2 runs go to `artifacts/runs/v2/<role>/`.
  - **Unchanged:** v1 code paths are unchanged, and v1 tests still pass.
- **One addition after the design above, before any paid call: the recovery exemption.**
  - **The problem:** when a request exceeds the hard limit, the existing runtime requires the very next step to shrink `context.json`, or the run ends. A required review would make that impossible in B and C.
  - **The rule:** an edit made while that over-limit recovery request is active needs no review. It is counted separately (`accepted_edits_recovery_exempt`), and the clause says so.
  - **Why it matters:** without it, B and C would be penalised by a rule A never meets.
- **Prompt version `2026-10-13.3`.**

  **B and C** (`INITIATED_REVIEW_V2_CLAUSE`):

  ```
CONTEXT EDITS NEED A REVIEW FIRST (this run):
- Before you edit context.json, start a context review. If new information may have made parts
  of your working context out of date, reply {"action": "begin_review", "purpose": "update",
  "new_information": "<that information, quoted or summarised>"}. If you only want to compact or
  reorganise the context, reply {"action": "begin_review", "purpose": "compaction"}.
- The runtime replies with the context revision and the entries to review (your notes and
  observations). The review authorises one context.json edit in a later step, until you make that
  edit, start another review, or the next round is released. You may also decide not to edit.
- An edit to context.json without a valid review is rejected and the previous context is kept;
  other effects of that code are not undone. A review uses one model call. Exception: when the
  runtime status says OVER LIMIT, edit context.json directly in that step; no review is needed.
  ```

  **C only** (`INITIATED_REVIEW_V2_JEV_CLAUSE`):

  ```
- In this run, each update review also asks a fast classifier (Jev), for each listed entry, for
  the probability that the new information requires reconsidering a current assertion or planned
  action in it (compaction reviews get no advice). The advice is probabilistic and can be wrong,
  and it never edits your context. A low probability is not a reason to delete an entry, and a
  high one does not mean the entry is wrong. You decide whether and how to edit.
  ```

- **Config:** `configs/exp010v2.toml`, which differs from `exp010.toml` only in `max_calls` 90, `max_reviews` 40, the `required` key (false, switched per run) and the ceiling.
- **Offline checks:**
  - **Tests:** `tests/test_pre_edit_review.py` has 13 tests, and all 56 Jev-related tests pass.
  - **Mutation check:** disabling the gate makes 4 v2 tests fail.
- **Scripted plumbing check:** run `…213429-clm_helpers-cacheon-prejev-rounds-dev-1-d6a9`, offline, with the real Docker sandbox, a scripted model and a fake Jev. It is **excluded from all results**.
  - **The direct edit:** blocked (step 2).
  - **The update review, then the edit:** accepted, with 1 Jev call.
  - **The compaction review:** not applicable, with no Jev call, and its edit was accepted after the next round's release.
  - **Totals:** 2 authorisations consumed, and 0 unauthorised accepted edits.

## v2 calibration record (2026-10-13, session 6)

- **Budget:** ceiling set from USD 89.687573 to USD 91.209294 (settled spend USD 61.209294, 0 pending, + 30).
- **Calibration:** comparison `20261012T213922`, 6/6 runs in the frozen rotation, all strict successes (14/14).
- **Gate outcome: FAILED on criterion 2.**
  - **The workflow was used:** B and C used it on every edit (48/48 accepted edits authorised; 0 blocked; 0 unauthorised; 0 recovery exemptions).
  - **But no review was applicable to Jev:** **all 48 started reviews were declared `compaction`**, so C made **0** applicable Jev reviews and **0** Jev calls.
  - **Friction:** B on dev-2 attempted 5 update reviews without `new_information` (each rejected with a notice) before using compaction.
- **As this protocol requires:** the runs are kept, prompts were not changed, development runs were not repeated, and `rounds-eval-9..12` were not registered. The 36-run evaluation was **not run**.
- **Projected evaluation cost:** about USD 18.9, which would have fitted.
- **Spend:** USD 2.515987 (Anthropic only, 253 calls). The ledger is at USD 63.725281 of USD 91.209294.
- **Analysis and v3 options:** in the README. Any v3 needs its own protocol revision and authorisation.
