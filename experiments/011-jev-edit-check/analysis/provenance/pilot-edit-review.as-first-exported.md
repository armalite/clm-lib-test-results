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

**Conclusion of the blind part:** no harmful context edit (rule-level loss or change) occurred in any condition. **Task-code changes and context-only changes** were made in separate steps or in the same step as the proposal. Code was always written (and tested) before the notes that describe it were compacted.
