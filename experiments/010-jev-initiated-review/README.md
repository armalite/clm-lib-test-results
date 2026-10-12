# 010 – Claude-initiated context review with Jev assistance (strategy 2)

**Status: implemented; stopped at the calibration readiness gate.** In all four calibration runs, in both conditions, Claude **never started a context review**. The question could therefore not be tested, and the 24-run evaluation was **not run**, as the protocol requires. No result here says anything about whether Jev's advice helps.

Part of the [Jev-assistance roadmap](../jev-assistance-roadmap.md). Protocol: [`protocol.md`](protocol.md) (the finalised section was written before any code or paid call).

## What 010 set out to test

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

## Implementation (available, opt-in)

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

## Spend

- **Calibration:** **USD 1.521721**, Anthropic only (130 calls; no TypeSafe calls), of the USD 30 authorised for 010.
- **Ledger:** USD 61.209294 spent of the USD 89.687573 ceiling, with nothing pending. The unused USD 28.48 does not carry over.

## Where is the evidence?

- `protocol.md`: the planned design, the finalised protocol and the session record.
- `report.md`, `metrics.json` and `metrics.csv`: the four calibration runs, with `ir_*` columns (all zero reviews).
- `artifacts/runs/calibration/<run_id>/`: requests (showing the clause, the schema and the status line), responses, context revisions and scores.
- `artifacts/comparisons/20261012T204507/`: the frozen settings, the schedule and the source patch.
