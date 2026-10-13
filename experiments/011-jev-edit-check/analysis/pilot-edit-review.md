# 011 agent pilot: edit-level review (exploratory)

**What this is:** the author's judgement, following the rubric in `../protocol.md` ("Edit-level analysis", written before the runs). It is not a scored outcome.

**Sources:**
- the pilot runs under `../artifacts/runs/pilot/`;
- the mechanical screen `pilot_analysis.py`.

## Part 1: written before any of the six runs' Jev verdicts were read

**Blinding, disclosed:**
- **During the runs:** the author saw only each run's status, cost, calls and edit count, plus the edit screen of run 1 (A, which has no Jev).
- **One verdict seen early:** while reviewing the only revision (C, w2-dev-2, P5 → P6), the author read the model's step-23 thought, "P5 flagged: sum5 omits that stage 5 tests passed and the code location". So **P5's verdict was seen before its classification**; every other classification below was made blind.
- **The smoke run's verdicts** (both clear) had been seen, but the smoke is excluded from every comparison.

**What was reviewed:**
- **Applied edits:** 26 in total:
  - A: 10 (5 per run);
  - B: 7 accepted proposals;
  - C: 8 accepted proposals.
- **Plus:** 1 revised (not applied) proposal.
- **Recovery-exempt edits:** 0.

For each applied edit, the post-edit notes were compared with the rules in force at that stage. The mechanical term screen found no requirement term (`viewer`, `include_archived`, `audit`, `since`, `exported_by`, `max_records`, `truncated`, and the partial-change terms) present before an edit and absent from the whole context after it.

| | A | B | C |
| --- | --- | --- | --- |
| Applied edits reviewed | 10 | 7 | 8 |
| **L at rule level** (a rule, exception or obligation in force absent afterwards) | **0** | **0** | **0** |
| L at sub-condition level (a detail of an already implemented rule absent afterwards) | in most edits | 1 proposal (w2-dev-1 P4) | 0 |
| Obligation `exported_by` written into notes before the stage-2 text was deleted | 2/2 runs | 2/2 | 2/2 |

**The sub-condition losses (L-detail).** Examples:
- **A, both instances:** the final notes say "max_records slice after sort" or "truncation after sort", not "after every other rule". They also omit "`truncated` false when `max_records` is absent", "header row alone when no records", "do not modify input" and "ignore unknown params".
- **B, w2-dev-1 P4:** "S5 NEW max_records slice + truncated bool key". The same two limit details are lost.

**In every case:**
- the code implementing the detail had already been written and its visible tests passed before the edit (the notes say so);
- the requirement files stayed readable, and A reread them near the end (step 14 or 15 in both A runs);
- the final hidden checks for the affected rules all pass.

**Classification: visibly lost detail, with no observed consequence.** No final failure exists to trace (all six runs pass 35/35), so the E/N/U classes for failures are empty.

**The revised proposal (C, w2-dev-2, P5).** Its stage-5 requirement text is **identical** to the accepted P6. P6 only adds "Stage 5 visible tests 2/2 OK (step 22)" and the exact implementation lines. **Classification: an acceptable proposal; the revision changed no requirement content** (P5's verdict not blind, as disclosed above).

**Conclusion of the blind part:** no harmful context edit (rule-level loss or change) occurred in any condition.

**Task code and context changes** (this sentence corrected after the step accounting in Part 2; it was vaguer as first written):
- **A:** wrote, tested and compacted in the same execution in 10/10 edits.
- **B:** proposed in the same step as a code change in 7/7.
- **C:** all 8 applied proposals came from context-only steps. The one proposal made in the same step as a code change (w2-dev-2 P5) was revised, not applied, and its code change stayed, as the protocol says.

## Part 2: after reading the verdicts

### Jev's verdicts and Claude's reactions (C only)

| Run | Proposal | lost | changed | evidence | insufficient | Verdict | Blind class | Reaction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w2-dev-1 | P1 | 0.27 | 0.19 | 0.44 | 0.46 | clear | acceptable | accepted |
| w2-dev-1 | P2 | 0.26 | 0.20 | **0.54** | 0.48 | **flagged** | acceptable | accepted, no stated reason |
| w2-dev-1 | P3 | 0.23 | 0.21 | 0.48 | 0.47 | clear | acceptable | accepted |
| w2-dev-2 | P1 | 0.27 | 0.10 | 0.40 | 0.29 | clear | acceptable | accepted |
| w2-dev-2 | P2 | **0.59** | 0.27 | **0.56** | 0.45 | **flagged** | acceptable | inspected, then accepted (thought quoted below) |
| w2-dev-2 | P3 | 0.31 | 0.25 | 0.46 | 0.43 | clear | acceptable | accepted |
| w2-dev-2 | P4 | 0.36 | 0.23 | 0.45 | 0.38 | clear | acceptable | accepted |
| w2-dev-2 | P5 | 0.39 | 0.31 | **0.51** | **0.63** | **flagged** | acceptable (not blind) | **revised** → P6 |
| w2-dev-2 | P6 | 0.40 | 0.30 | **0.54** | **0.60** | **flagged** | acceptable | accepted |

**Counts:**
- **Checks:** 9, with **0 errors**, 0 retries, 0 incomplete and 0 not checked.
- **Verdicts:** 4 flagged and 5 clear. There were 0 uncertain-only verdicts, and `evidence_notes` was empty for all 9 (no missing output, truncation or unresolved citation).
- **`insufficient` ≥ 0.5:** 2 checks (P5, P6), both also harm-flagged, so the shown result was FLAGGED.

**Classification of the flags:**
- **Useful warnings** (a harmful proposal flagged and then corrected): **0**. No harmful proposal occurred.
- **False alarms** (an acceptable proposal flagged): **4 of 4 flags.**
- **Advice not acted on:** 3 flagged proposals were accepted. This was correct by the blind review: the advice was ignored appropriately.
- **Unnecessary revision:** 1 (P5 → P6). It added only a test-status line and implementation detail; P6 was flagged again (`evidence` 0.54) and then accepted.

**Pattern (post hoc):**
- **`evidence` sat near the threshold for every proposal** (0.40–0.56). Every proposal deleted the raw step entries (code, test output, receipts) that the new summary note replaces. That is the removal of tool output that the v2 questions treat as possible evidence loss.
- **The single `lost` flag (0.59, w2-dev-2 P2)** coincides with removing a completed "Next: advance to stage 2" line from a note. It resembles v1's `c02`, removal of a completed item.

**Example of a reasoned reaction** (C, w2-dev-2, step 9, `confirm_edit` P2 accept):
> "Jev flagged P2, so I checked it. sum2 restates both stage 2 rules: the status filter, and the exported_by obligation if the format ever moves off CSV. The stage 1 summary is unchanged except for a stale 'next' note. The removed entries are only the raw transcript that these summaries cover, so I'm accepting."

**Example of an unnecessary revision** (C, w2-dev-2, step 23):
> "P5 flagged: sum5 omits that stage 5 tests passed and the code location. Revising the proposal to record both before accepting."

### Intervention coverage and the OVER LIMIT exception

| | B (2 runs) | C (2 runs) |
| --- | --- | --- |
| Content-changing context writes | 7 | 9 (8 applied + 1 revised) |
| Held as proposals | 7 | 9 |
| Applied by explicit accept | 7 | 8 |
| **Applied directly under the OVER LIMIT exception (bypassing confirmation)** | **0** | **0** |
| Jev-checked | — | 9 / 9 |
| **Edits that bypassed Jev in C** | — | **0** |
| Already-checked proposals bypassed | — | 0 |
| OVER LIMIT recovery requests | 2 (1 per run) | 2 (1 per run) |
| Resolved by accepting the pending proposal | 2 | 2 |

**Notes:**
- **Every recovery request in B and C** occurred while a shrinking proposal was pending, and was answered with `confirm_edit` accept.
- **The pre-freeze status-line fix was effective here:** it names the pending proposal under OVER LIMIT, after the smoke had shown the bypass.
- **A had 0 recovery requests** and 0 pressure steps. A compacted in the same execution that wrote the code.
- **Coverage did not differ between B and C,** and no bypass limited the comparison.
- **Withdrawals:** none, so the "other files remain" path was not exercised in the pilot (it is covered by tests).

### Information lost, never recorded, or not used

- **Lost at rule level in an applied edit:** none (Part 1).
- **Lost at detail level:** A in most edits and B once. There was no observed consequence: all hidden checks pass, the code was already written and tested, and the files stay rereadable. A reread the requirement files once near the end of each run.
- **Never recorded:** not observed. Every stage's text entered the context at release, and each rule was summarised before its stage text was removed.
- **Present but used incorrectly:** not observed (no hidden-check failure in any run).
- **What the evidence supports:** no final task result can be attributed to a context edit, and none needs to be, since all runs pass.
