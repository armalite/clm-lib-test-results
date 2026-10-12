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
