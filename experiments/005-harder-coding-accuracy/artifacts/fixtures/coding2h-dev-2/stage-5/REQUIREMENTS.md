# Stage 5 of 8 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [CHANGED] Bulk lines (partly replaces the stage-3 rule): a line is now a bulk line when qty >= 50. The 0.90 multiplier and everything else about bulk lines are unchanged.
- [CHANGED] Validation (partly replaces the stage-2 rule): a line with qty 0 is now allowed and ignored entirely. If every line is ignored, raise ValueError as for an empty list. All other validation from stage 2 is unchanged.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
