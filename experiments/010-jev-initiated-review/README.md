# 010 – Claude-initiated context review with Jev assistance (strategy 2)

**Status: complete (protocol v3).** Three protocol versions, reported separately and never pooled:

| Version | Design | Outcome |
| --- | --- | --- |
| **v1** | Review optional | Stopped at the calibration gate: Claude never started a review |
| **v2** | Review required before every edit; Claude's "update"/"compaction" label decided whether Jev ran | Stopped at the calibration gate: every review was labelled "compaction", so Jev never ran |
| **v3** | The same required review, but the **runtime** supplies the update (the latest released round's board and change-log lines), so Jev runs whenever an update and entries exist | Smoke, calibration and gate passed; **36-run evaluation completed** |

**v3 headline (4 fresh instances × 3 repetitions):**
- **Jev's increment within the review workflow (C vs B):** essentially nothing measurable. Cost was −2% (cheaper in 6 of 12 blocks), time −1 s, and correctness identical (12/12 in both).
- **The review workflow itself (B vs A, C vs A):** about 30% more cost, 42 s more time and 11–13 more calls per run.
- **Strict success:** 12/12 in B and C against 10/12 in A, but this is not established (sign test p = 0.5). A's two failures were adjacent-line miscitations of one early change record.
- **Verdict:** on this workload the benefit does not justify the overhead.

Evidence: `artifacts/runs/calibration/` (v1), `artifacts/runs/v2/` and `artifacts/runs/v3/`. The v2 audit is in [`analysis/`](analysis/v2-review-audit.md).

# Protocol v1: optional Claude-initiated review (2026-10-13, session 5)

## What 010 v1 set out to test

**The question:** when Claude itself decides that its working context needs review, does Jev's advice, delivered automatically as part of that review, improve the resulting agent performance?

**The scenario:** the task is a **fictional** multi-service incident from the synthetic generator `incident-rounds-gen/1`. Evidence (logs, incident-board updates, change records) arrives over 10–11 hourly rounds, and the agent must report the real incidents with causes, services, statuses and file:line evidence.

**Both conditions** have the same `begin_review` action and the same instruction (protocol: `INITIATED_REVIEW_CLAUSE`). When Claude judges that new information may have made parts of its context out of date, it can reply `{"action": "begin_review", "new_information": "..."}`.
- **What the runtime returns:** the current context revision and the entries to review (notes and observations). It does not list step-action or receipt entries.
- **What happens next:** Claude decides, in its next step, whether and how to edit.
- **Cost of a review:** one model call. Editing without a review is always possible.

**The assisted condition** gets the same, plus Jev's per-entry probability (the fixed `jev-review/1` question against the stated new information). The probabilities are computed before Claude's next turn and are advisory only.

**How this differs:**
- **From 008:** in 008, Claude had to choose to call Jev itself; here, Jev comes with every review.
- **From 009:** in 009, a review ran at every update.

The control is "CLM with the initiated-review protocol", not any earlier control.

## Calibration (comparison `20261012T204507`)

**Setup:** two development instances (`rounds-dev-1`, `rounds-dev-2`, already used by 007–009) × two conditions, in the order dev-1 A, B; dev-2 B, A. The settings are the same as 009's runtime: `claude-opus-5-5`, effort low, an 8,000-token request budget, 60 task calls, 5-minute caching, and a cold isolated cache per run.

| | A dev-1 | B dev-1 | B dev-2 | A dev-2 |
| --- | --- | --- | --- | --- |
| Run id | `…204507…rev-rounds-dev-1-ded2` | `…204745…revjev-rounds-dev-1-d831` | `…205002…revjev-rounds-dev-2-54c2` | `…205241…rev-rounds-dev-2-fa6c` |
| **Reviews started** | **0** | **0** | **0** | **0** |
| Strict success (checks) | S (14/14) | S (14/14) | F (13/14) | F (13/14) |
| Cost USD (Anthropic; no Jev calls) | 0.383 | 0.326 | 0.426 | 0.387 |
| Elapsed / Anthropic time (s) | 158 / 122 | 137 / 104 | 159 / 123 | 164 / 126 |
| Model calls / executions / accepted edits | 32 / 22 / 14 | 30 / 20 / 12 | 34 / 23 / 15 | 34 / 23 / 12 |
| Context-pressure steps | 5 | 2 | 4 | 5 |
| Tokens: uncached / cache read / cache write / output | 4,170 / 107,547 / 39,056 / 7,465 | 3,801 / 104,586 / 32,286 / 6,413 | 4,379 / 121,032 / 44,032 / 8,230 | 4,419 / 118,486 / 39,097 / 7,490 |

**Clean execution:** no repairs, retries, recoveries or rejected edits. No Jev call was made, because no review was started.

**Correctness failures** (kept, development instances):
- **B dev-2:** it missed thread A's status evidence. The answer cited `round-08/board.md:4` instead of `:3`.
- **A dev-2:** it missed thread C's cause evidence, and cited a log range that was invalid.

**Not a comparison:** with zero reviews, the two conditions differed only in one unused prompt paragraph. These cost and time figures are calibration data, not evidence about Jev.

## Readiness gate: FAILED

| Gate criterion (predeclared) | Outcome |
| --- | --- |
| 1. Both conditions initiate reviews (at least one each; at least 4 in total) | **Failed: 0 reviews in 4 runs** |
| 2. Reviews come while work remains | **Failed: none** |
| 3. Assisted path works live (real Jev calls, advice before edits) | Not exercised: no reviews |
| 4. Edits govern requests; accounting, caching, scoring and export work | Passed (export checksums verify) |
| 5. No material implementation defect | None found |
| 6. Projected evaluation fits the budget (about USD 0.38 × 24 × 1.25 ≈ 11.4, against about USD 28.5 remaining) | It would have fitted |

**As the protocol requires:**
- the runs are kept;
- the instructions were **not** strengthened;
- no forced-use runs were substituted;
- no evaluation instances were registered or run.

### Diagnosis

- **The mechanism was fully exposed.** In every request:
  - the system prompt carried the review clause (and, in B, the Jev explanation);
  - the structured-output schema listed `begin_review` as an allowed action;
  - the status line showed "context reviews used 0/12".
- **Claude chose direct edits instead.** It made 12–15 accepted context edits per run, consolidating each round's board and log findings into its notes with `execute`. That is exactly what the instruction allows ("You can edit context.json at any time without a review").
- **It never mentioned a review.** No response mentioned or reasoned about one; the only "review" text in the traces is the task's CAPACITY_REVIEW follow-up.
- **The likely reading:** an optional extra step that costs a model call is not adopted when the model already integrates updates by direct editing. This matches 008, where an optional Jev tool was never used.
- **What 010 measured:** the use of the shared review step, which was zero. It measured nothing about Jev, which never had the chance to act.

### Exploratory note on the two omissions (scorer unchanged)

- **B dev-2:** the expected status line was cited in Claude's notes through the last context revision, but the answer cited the adjacent line. The information was present in context and **miscited at answer time**, not lost in an edit.
- **A dev-2:** the expected cause-log lines never appeared in the notes, so the evidence was **never recorded**. It was not lost in a later edit.

### Options for a revised protocol (not done; each would need its own protocol revision and authorisation)

- **Make review the route for certain edits:** for example, require `begin_review` before an edit that removes or rewrites a note. This moves toward 011, the proposed-edit check.
- **Remove the extra turn:** let Claude attach a review request to an ordinary `execute` action, so the advice arrives before the following step. This changes what "before the edit" means and would need careful design.
- **A stronger instruction:** describe when a review is expected. This changes the question from "when Claude decides" toward "when instructed", and must be labelled as such.

## v1 implementation (available, opt-in)

`initiated-review/1` is implemented in clm-lib (SPEC §21), off by default:
- the conditions `+rev` and `+rev-jev`;
- the review step on the host;
- current-revision candidates by the structural role rule;
- Jev advice before Claude's next turn;
- rejection limits;
- per-review records linking each review to later accepted edits;
- advice-residence measurement;
- `ir_*` export columns.

**Tests:** 10 focused tests cover the trigger and condition differences, advice before the edit, current-revision and deleted-entry handling, no future or hidden information, service failures and accounting, residence and stale labelling, and export. They pass in the full suite (181 tests).

**Limitation:** the live in-loop Jev path of this new action is unexercised. It shares 009's scoring code, which made 117 successful live calls.

## v1 spend

- **Calibration:** **USD 1.521721**, Anthropic only (130 calls; no TypeSafe calls), of the USD 30 authorised for 010.
- **Ledger:** USD 61.209294 spent of the USD 89.687573 ceiling, with nothing pending. The unused USD 28.48 does not carry over.

## v1 evidence

- `protocol.md`: the planned design, the finalised protocol and the session record.
- `report.md`, `metrics.json` and `metrics.csv`: the four calibration runs, with `ir_*` columns (all zero reviews).
- `artifacts/runs/calibration/<run_id>/`: requests (showing the clause, the schema and the status line), responses, context revisions and scores.
- `artifacts/comparisons/20261012T204507/`: the frozen settings, the schedule and the source patch.

---

# Protocol v2: required pre-edit review (2026-10-13, session 6)

## What v2 changed and why

**Why a v2:** v1 let Claude bypass the review and edit directly, which it always did. v2 tests a different question:

**When Claude decides to edit its working context, does a Jev-assisted review improve the outcome enough to justify its overhead?**

It is not another test of voluntary adoption: in B and C, every context edit must follow a review.

**Conditions:**

| | Condition | Workflow |
| --- | --- | --- |
| A | Ordinary CLM (`clm_helpers:on`) | Direct editing, with no review and no Jev |
| B | Required pre-edit review, no Jev (`+pre`) | Claude starts `begin_review` (purpose `update` with the new information, or `compaction`), receives the current revision's entry ids, then edits in a later step |
| C | The same, with Jev (`+pre-jev`) | Identical to B. Update reviews also return Jev's per-entry advice before the edit; compaction reviews are "not applicable" |

**How the requirement works:**
- **One authorisation per review:** a review issues one edit authorisation, bound to the reviewed entries.
- **What survives:** runtime appends between the review and the edit leave it valid.
- **How it ends:** an accepted edit consumes it; a new review replaces it; the next round's release expires it; a change to a reviewed entry invalidates it.
- **Without an authorisation:** a content-changing write to `context.json` is rejected through the normal rejection path. The code still ran once; nothing is executed twice or rolled back.
- **Recovery exemption:** in an over-limit recovery step, a review is not required.

All limits are equal across A, B and C: 90 main-model calls (raised from 60) and 40 reviews. The other settings are 009's runtime. Full details are in the protocol's "Protocol v2" section.

**Predeclared contrasts:**
- **C vs A:** the deployed Jev workflow vs ordinary CLM.
- **C vs B:** Jev's increment within the workflow.
- **B vs A:** the workflow's own effect and overhead.

## What ran

- **Offline checks:** 13 focused tests (194 in the full suite). Disabling the gate makes 4 of them fail.
- **A scripted plumbing check:** real sandbox, scripted model, fake Jev; excluded from results.
- **Calibration:** comparison `20261012T213922`, 2 development instances × 3 conditions, in the rotation dev-1 A, B, C; dev-2 B, C, A.
- **Deviations:** none. The only design addition, the recovery exemption, was made **before** any paid call and is recorded in the protocol.

## Calibration results (development instances; not an evaluation)

| | A dev-1 | B dev-1 | C dev-1 | B dev-2 | C dev-2 | A dev-2 |
| --- | --- | --- | --- | --- | --- | --- |
| Run id suffix | `…213922…rounds-dev-1-e281` | `…214136…pre-…dev-1-e65c` | `…214420…prejev-…dev-1-be06` | `…214717…pre-…dev-2-7605` | `…215102…prejev-…dev-2-fcf2` | `…215429…rounds-dev-2-a775` |
| Strict success (checks) | S 14/14 | S 14/14 | S 14/14 | S 14/14 | S 14/14 | S 14/14 |
| Cost USD (all Anthropic) | 0.314 | 0.353 | 0.432 | 0.498 | 0.494 | 0.426 |
| Elapsed / Anthropic time (s) | 135 / 104 | 164 / 130 | 177 / 142 | 226 / 184 | 207 / 168 | 169 / 128 |
| Model calls | 29 | 39 | 44 | 56 | 48 | 37 |
| Accepted edits (all authorised in B/C) | 9 | 9 | 12 | 14 | 13 | 16 |
| Reviews: update / compaction / rejected | — | 0 / 9 / 0 | 0 / 12 / 0 | 0 / 14 / 5 | 0 / 13 / 0 | — |
| **Jev calls** | — | — | **0** | — | **0** | — |
| Context-pressure steps / recovery requests | 3 / 0 | 15 / 0 | 20 / 2 | 23 / 1 | 23 / 3 | 6 / 0 |
| Tokens: uncached / cache read / cache write / output | 3,427 / 94,623 / 30,917 / 6,322 | 6,354 / 161,518 / 32,682 / 6,570 | 7,391 / 193,841 / 44,150 / 7,166 | 9,234 / 242,778 / 49,394 / 8,267 | 8,149 / 214,351 / 48,243 / 8,860 | 4,462 / 116,408 / 46,259 / 7,664 |

**Calibration means (two instances each; not evidence of an effect):**

| | A | B | C |
| --- | --- | --- | --- |
| Cost (USD) | 0.370 | 0.425 | 0.463 |
| Elapsed (s) | 152 | 195 | 192 |
| Calls | 33 | 47.5 | 46 |

**Clean execution:** no edit was blocked or made without authorisation, and no recovery exemption was used. The six recovery steps in B and C were edits covered by existing authorisations. There were no repairs and no API retries.

**Per contrast (calibration only):**
- **B vs A:** the required review added about 15% cost, 28% elapsed time and 44% more calls. It raised context-pressure steps about fourfold (from 4.5 to 19 per run), because review observations accumulate in context.
- **C vs B:** no Jev call ever happened, so the differences are run-to-run variation, not a Jev effect.
- **C vs A:** C's extra cost here comes entirely from the review workflow.

## Readiness gate: FAILED

| Gate criterion (predeclared) | Outcome |
| --- | --- |
| 1. B and C use the review-before-edit workflow | **Passed:** 48/48 accepted edits authorised by a prior review; 0 bypasses |
| 2. C makes at least 2 applicable (update) Jev reviews before the last round | **Failed: 0.** All 25 of C's reviews were declared compaction |
| 3. Advice arrives before subsequent edits | Not exercised: no advice |
| 4. No bypass, revision or accounting defect | Passed |
| 5. Accounting, caching, scoring and export work | Passed (checksums verify; v1 rows unchanged) |
| 6. The evaluation would fit (about USD (0.370 + 0.425 + 0.463) × 12 × 1.25 ≈ 18.9, against USD 27.48 remaining) | It would have fitted |

**As the protocol requires:**
- the runs are kept;
- prompts were **not** changed;
- development runs were not repeated;
- `rounds-eval-9..12` were not registered, and the 36-run evaluation was not run.

### Diagnosis

**Claude labelled every review "compaction".** It did so even when the edit that followed folded newly read round findings into its notes, with thoughts such as "Compact with R3 findings" and "fold R4 findings into n1". In this workload Claude's routine edit is a per-round consolidation, and it treats that as compaction.

**The purpose split gave Claude a way to avoid stating new information.** The split was needed so that Jev is not asked a question that does not apply to pure compaction. Its consequence was that **Jev was never applicable**. This is a design limitation of v2, not a Jev result.

**A friction point:**
- **What happened:** B on dev-2 sent five update reviews in a row **without** `new_information`, each rejected with a notice (5 extra calls), before switching to compaction.
- **Why:** the shared action schema cannot make that field conditionally required, and Claude omitted it.

**Overhead remains real** even with Jev inactive: a required review per edit added calls, time and context pressure.

### Options for a v3 (not done; each needs its own protocol revision and authorisation)

1. **Runtime-supplied update source.** At a required pre-edit review, the "new information" would be the evidence released since the previous review: the 009 `round-files/1` payload, mechanical and identical in B and C. Claude no longer classifies reviews, and Jev is applicable whenever new evidence exists. This keeps the trigger as Claude's edit decision (unlike 009, which reviewed at every release).
2. **Always state the new information:** remove the compaction purpose and require `new_information`, allowing an explicit "none" that is recorded as not applicable. This still depends on Claude's classification.
3. **Make `new_information` required in the schema for update reviews:** a separate action name, for example. This fixes the friction point only.

## Representative trace (C, dev-2: `…215102…prejev-rounds-dev-2-fcf2`, fictional scenario)

- **Step 10:** Claude replies `{"action": "begin_review", "purpose": "compaction"}`.
- **The review material:** revision, candidate ids, and "Context review advice: not applicable (compaction review: no new information stated)".
- **Step 11:** an `execute` with the thought *"Compact with R3 findings."* rewrites the note with round-3 board and log findings. The edit is accepted and authorised by the step-10 review.
- **What was missed:** new evidence was incorporated without an update review, so Jev never assessed whether that evidence made earlier notes out of date.

No advice existed, so there are no examples of advice followed, ignored or misleading.

## v2 implementation (available, opt-in; SPEC §21)

- `initiated-review/2`;
- the conditions `+pre` and `+pre-jev`;
- the authorisation gate in `ContextStore.read_back`;
- the v2 summary fields (reviews by purpose, blocked and authorised edits, authorisation outcomes);
- `ir_*` v2 export columns;
- the optional export group.

v1 behaviour is unchanged.

## v2 spend

- **Calibration:** **USD 2.515987**, Anthropic only (253 calls; no Jev calls), of the USD 30 authorised for v2.
- **Ledger:** USD 63.725281 spent of the USD 91.209294 ceiling, with nothing pending. The unused USD 27.48 does not carry over.

## v2 evidence

- `protocol.md`: the "Protocol v2" section, the pre-run session record and the v2 calibration record.
- `report.md`, `metrics.json` and `metrics.csv`: the rows with phase `v2-calibration`, including `ir_version`, `ir_reviews_update`, `ir_reviews_compaction`, `ir_edits_authorised` and `ir_edits_blocked`.
- `artifacts/runs/v2/calibration/<run_id>/`: requests (showing the clause, the schema and the authorisation status line), responses, review observations, context revisions, rejected bytes and scores.
- `artifacts/comparisons/20261012T213922/`: the frozen settings, the schedule and the source patch.

---

# Protocol v3: required pre-edit review with a runtime-supplied update (2026-10-13, session 7)

## Why v3, from the v2 audit

The offline audit of all v2 reviews is in [`analysis/v2-review-audit.md`](analysis/v2-review-audit.md); its classifications are exploratory.
- **The labels:** all 48 v2 reviews were labelled "compaction", so C skipped Jev at all 25 of its reviews.
- **The edits:** 36 of the 48 authorised edits incorporated newly released findings.
- **The inputs:** a released board or change-log update existed at 42 of 48 reviews, and candidate entries at all 48.
- **The mismatch:** Claude's label, not the content of its edits, decided whether Jev ran.

## What v3 changed (and nothing else)

- **The review action** is `{"action": "begin_review"}`. A `purpose` label and a `new_information` note are optional and **recorded only**.
- **The update** is supplied by the runtime: the latest released round's incident-board and change-log lines (009's `round-files/1`; verbatim, line-referenced, logs excluded, capped at 4,000 characters).
  - **The review material names it** (round, files, line count, hash) rather than quoting it, so B and C see no evidence A cannot read from the same files.
- **C calls Jev whenever** that update is non-empty and the current revision has candidate entries, regardless of the label. Otherwise the review is recorded as not applicable, with a reason.
- **Unchanged from v2:**
  - the required review before every edit;
  - one-use authorisation bound to the reviewed entries (it ends on consumption, replacement, expiry at the next round or invalidation);
  - bypass rejection and the recovery exemption;
  - the candidate rule, the Jev question (`jev-review/1`) and model (`jev-1.13.0`), and the advice format;
  - limits (90 calls and 40 reviews for all conditions), caching and the scorer.

**Conditions:**
- **A:** ordinary CLM (`clm_helpers:on`).
- **B:** the required review without Jev (`+pre3`).
- **C:** the same with Jev (`+pre3-jev`).

## What ran

- **Offline:**
  - **Tests:** 10 focused tests (204 in the suite).
  - **Mutation check:** making "compaction" skip Jev again fails a test.
  - **A scripted plumbing check** through the real sandbox; excluded.
- **Live smoke** (`v3-smoke`, excluded), `…225935…pre3jev-rounds-diag-1-f4c4`:
  - **Reviews:** 13, all labelled "compaction". Jev advised the 12 applicable ones (the 13th had an empty update).
  - **Request contents:** each request held exactly the latest-round update and the current entries.
  - **Ordering:** the advice preceded every authorised edit.
- **Calibration** (comparison `20261012T230436`, **reused** development instances, 6 runs): the gate **passed**.
  - **Edits:** all 44 accepted B/C edits were authorised by reviews.
  - **Jev:** C was advised at 19 of 19 applicable reviews.
  - **No defect** was found.
  - **Projected evaluation cost:** USD 20.19, against USD 26.77 remaining.
- **Evaluation** (comparison `20261012T232533`): `rounds-eval-9..12` (fresh, registered after the gate) × 3 repetitions × 3 conditions = **36/36 runs**.
  - **Clean execution:** no halts, repairs, retries or invalid runs; 131 of 131 applicable C reviews advised; 131 Jev calls with no errors.
  - **Order:** balanced, with each condition 4 times in each position.
  - **Provenance:** the code matched the frozen patch byte for byte.
- **Deviations:** none.

## Evaluation results (12 runs per condition; mean, with median in brackets)

| | A: ordinary CLM | B: required review | C: required review + Jev |
| --- | --- | --- | --- |
| **Strict success** | **10 / 12** | **12 / 12** | **12 / 12** |
| Checks passed | 166 / 168 | 168 / 168 | 168 / 168 |
| … evidence (other categories all full in every condition) | 34 / 36 | 36 / 36 | 36 / 36 |
| Stale causes or statuses | 0 | 0 | 0 |
| **Total cost per run (USD)** | **0.348** (0.335) | **0.457** (0.435) | **0.448** (0.431) |
| of which Jev (TypeSafe) | — | — | 0.0012 |
| **Elapsed per run (s)** | **151.5** (149.1) | **195.0** (186.9) | **193.9** (185.3) |
| Anthropic time / Jev time (s) | 115.0 / — | 154.1 / — | 151.0 / 2.7 |
| Main-model calls | 32.5 | 45.9 | 43.8 |
| Accepted context edits | 11.7 | 12.1 | 11.1 |
| Reviews (all labelled "compaction" except one per arm) | — | 12.2 (146 in total) | 11.1 (133 in total) |
| Reviews of an already-reviewed round / with an empty update | — | 25 / 3 | 15 / 2 |
| Jev: applicable reviews advised / entries answered of scored | — | — | 131 / 131 · 680 / 680 |
| Jev input tokens / advice characters per run | — | — | 28,433 / 3,948 |
| Context-pressure steps / recovery requests / spills | 2.1 / 0 / 0 | 19.2 / 1.0 / 1.1 | 18.8 / 2.3 / 1.2 |
| Tokens: uncached / cache read / cache write / output | 3,789 / 105,305 / 35,090 / 6,818 | 7,592 / 194,365 / 43,426 / 8,548 | 7,317 / 190,691 / 42,724 / 8,308 |
| Repairs / API retries / rejected or blocked edits | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |

**Failures** (kept; both A, both the same kind):
- **eval-11 rep 3:** thread C's origin evidence (the early change record) was missing; the answer cited `round-01/changes.md:3` instead of `:4`.
- **eval-12 rep 3:** the same.

**Exploratory note:** in eval-11 the expected line was in A's notes through the last revision, so it was miscited at answer time. In eval-12 it never appeared in the notes. Neither is a loss in an edit.

## The three contrasts (12 matched blocks each)

| Contrast | Cost | Time and calls | Strict success |
| --- | --- | --- | --- |
| **C vs A** (deployed Jev workflow vs ordinary CLM) | **+29%** on means (paired median +30%); C cheaper in **1 of 12** | +42 s and +11 calls per run; C faster in 0 of 12 | only C: 2, only A: 0, both: 10 (p = 0.5) |
| **C vs B** (Jev's increment) | **−2%** on means (paired median −2%); C cheaper in 6 of 12 | −1 s and −2 calls; faster in 7 of 12 | identical: 12/12 both |
| **B vs A** (the review workflow) | **+31%** on means (paired median +29%); B cheaper in 2 of 12 | +43 s and +13 calls; faster in 0 of 12 | only B: 2, only A: 0 (p = 0.5) |

**Per instance** (mean of 3 repetitions; four task instances, not twelve independent designs):

| Instance | Strict A / B / C | Cost A / B / C (USD) | Elapsed A / B / C (s) | Calls A / B / C |
| --- | --- | --- | --- | --- |
| eval-9 | 3/3 · 3/3 · 3/3 | 0.327 / 0.456 / 0.421 | 145 / 188 / 183 | 30.7 / 46.0 / 39.7 |
| eval-10 | 3/3 · 3/3 · 3/3 | 0.364 / 0.425 / 0.418 | 153 / 184 / 185 | 34.0 / 42.7 / 42.3 |
| eval-11 | 2/3 · 3/3 · 3/3 | 0.388 / 0.533 / 0.522 | 166 / 231 / 224 | 35.7 / 54.0 / 50.0 |
| eval-12 | 2/3 · 3/3 · 3/3 | 0.313 / 0.415 / 0.433 | 141 / 177 / 184 | 29.7 / 41.0 / 43.0 |

**Order:** no consistent order effect. Mean cost by position: A 0.344 / 0.385 / 0.314; B 0.427 / 0.449 / 0.497; C 0.473 / 0.435 / 0.438.

## What coincides with the differences (observed, not proven causes)

- **The workflow's overhead** (B and C vs A):
  - **Extra calls:** each edit costs at least one extra call (the review), giving about 12 more calls per run.
  - **Larger context:** review observations sit in context, so pressure steps rose about ninefold (2.1 → 19) and cache reads almost doubled.
  - **Repeat reviews of the same round** happened 25 times in B and 15 in C.
- **Jev's own cost** is negligible: USD 0.0012 and 2.7 s per run, about 0.3% of C's cost.
- **C vs B:** cost, time, calls, edits and correctness all coincide. **No incremental effect of the advice is visible.**
- **A's two misses vs none in B and C:** both are adjacent-line citation errors on one early change record, on two different instances in repetition 3. With 2 discordant blocks this is far from conclusive, and it cannot be attributed to the advice, since B, without Jev, also avoided them.

## Advice and edits (C; temporal association only)

**Counts:**
- **Flags:** of 680 scored entries, 126 were flagged at 0.5 (13 on runtime observation entries).
- **What followed:** 98 flagged entries were changed by the next authorised edit and 28 were not. 420 unflagged entries were also changed; Claude routinely rewrites its notes and deletes runtime entries.
- **Residence:** advice observations were carried in about one later request each (133 over 131 reviews), because Claude usually deleted them at the next edit.

**Examples** (fictional scenario; trace ids shortened):

1. **Advice followed by a relevant edit** (eval-9 rep 1, `…233137…pre3jev-rounds-eval-9-218f`, round 7).
   - **The update:** *"Thread B root cause revised: … (DISK_PRESSURE); this supersedes the earlier suspicion of DB_POOL_EXHAUSTED"* and *"Thread D closed: false alarm"*.
   - **Jev:** `n4` 0.81 (*"Thread B shipping-svc DB_POOL_EXHAUSTED ongoing"*) and `n5` 0.92 (*"Thread D CERT_EXPIRED … ongoing"*); other notes 0.09–0.21.
   - **Claude's edit:** `n4` became *"Thread B shipping-svc (cause later revised)"* and `n5` *"Thread D CERT_EXPIRED was FALSE ALARM (round-07/board.md:4)"*, and a round-7 note was added.
   - **Why it shows no causation:** the same edit also rewrote the unflagged notes `n1`–`n3`, so the advice did not set the edit's scope.
2. **Advice ignored** (eval-11 rep 1, `…234312…pre3jev-rounds-eval-11-580c`, round 6).
   - **The update:** thread A mitigated; VENDOR_TICKET closed.
   - **Jev:** `n3` 0.66 (*"Thread A … ongoing"*) and `n4` 0.50.
   - **Claude** left both unchanged and added `n6` (*"Thread A mitigated (CHG-150 …); CLOSED VENDOR_TICKET"*), keeping a newest-note-wins log.
   - **Outcome:** the run still succeeded.
3. **Redundant advice:** across the runs, flags on runtime observation entries (13) and on rolling notes that Claude rewrites every round add text without changing what Claude does. The C vs B equality is consistent with that.
4. **Misleading advice:** no clear case of a flag leading to a wrong edit was found. This category is not filled by invention.

## Conclusions (v3)

- **C vs A:** the Jev-assisted workflow cost about 29% more and took about 28% longer than ordinary CLM. Its 12/12 vs 10/12 strict success is not established.
- **C vs B:** Jev added nothing measurable within the review workflow, in cost, time, calls or correctness.
- **B vs A:** the required review workflow is the source of all the overhead. Any accuracy difference is small, from two blocks, and not established.
- **Does the benefit justify the overhead?** **No, on this workload.** The extra USD 0.10 and 42 s per run bought, at most, two avoided citation errors in 12 blocks, and Jev's advice had no measurable share in that.
- **Not claimed:** generality beyond this synthetic incident family, this model, this effort setting and this question; or novelty.

## v3 spend

- **Total: USD 18.277976** of the USD 30 authorised (Anthropic 18.260253, TypeSafe 0.017723):

  | Phase | Anthropic | TypeSafe |
  | --- | --- | --- |
  | Smoke | 0.539724 | 0.001394 |
  | Calibration | 2.690117 | 0.001995 |
  | Evaluation | 15.030412 | 0.014334 |

  The evaluation made 1,466 Anthropic calls and 131 Jev calls.
- **Ledger:** USD 82.003257 of the USD 93.725281 ceiling, with nothing pending. The unused USD 11.72 does not carry over.

## v3 evidence

- `protocol.md`: the "Protocol v3" section, the pre-run record, the smoke, the calibration and gate, the evaluation freeze, and the execution notes.
- `analysis/`: the v2 applicability audit.
- `report.md`, `metrics.json` and `metrics.csv`: the phases `v3-smoke`, `v3-calibration` and `v3-evaluation`, with `ir_update_source`, `ir_reviews_applicable` and `ir_reviews_repeat_round`.
- `artifacts/runs/v3/{smoke,calibration,evaluation}/<run_id>/`, per run:
  - every review's update payload and hash, its candidates and Jev answers;
  - `jev/NNNN.json` requests and responses;
  - requests, context revisions and scores.
- `artifacts/comparisons/20261012T230436/` and `…232533/`: the frozen settings, the schedules and the source patches.
