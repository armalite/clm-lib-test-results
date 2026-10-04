# Stage 4 of 6 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [NEW] Bulk and tier discounts do not stack: bulk lines are not tier-eligible. The tier-eligible amount is the sum of the line amounts of the lines that are not bulk lines.
- [CHANGED] Tax (partly replaces the stage-1 rule): customers with region 'NZ' are now taxed at 15% and region 'US' at 0%. Every other region keeps the stage-1 rate.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
