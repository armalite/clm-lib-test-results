# Stage 6 of 6 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [CHANGED] Tax (partly replaces the stage-3 rule): customers with region 'NZ' are now taxed at 15% and region 'US' at 0%. Every other region keeps the stage-3 rate.
- [CHANGED] Tier discount (partly replaces the stage-1 rates): the 'gold' rate is now 8%, and a new tier 'platinum' gets 10%. The 'silver' rate, the 0% for other tiers and the rest of the tier discount rule are unchanged.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
