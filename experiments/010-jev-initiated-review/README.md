# 010 – Claude-initiated context review with Jev assistance (strategy 2)

**Status: two protocol versions, both stopped at their calibration readiness gates. No evaluation was run, and no result here says whether Jev's advice helps.**
- **Protocol v1** (review optional): Claude never started a review; it edited directly in all four runs.
- **Protocol v2** (review required before every context edit): the workflow worked, with every accepted edit preceded by a review and none bypassed. But Claude declared every one of its 48 reviews a *compaction* review, so Jev was never applicable and made **no** calls. The Jev condition was therefore identical in practice to the review-only condition.

The two versions are reported separately below and never pooled. v2 evidence is in `artifacts/runs/v2/`, with phase `v2-calibration`.

Part of the [Jev-assistance roadmap](../jev-assistance-roadmap.md). Protocol: [`protocol.md`](protocol.md) (the finalised section was written before any code or paid call).

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
