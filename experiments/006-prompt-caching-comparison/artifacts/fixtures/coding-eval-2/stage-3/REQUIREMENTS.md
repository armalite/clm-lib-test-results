# Stage 3 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Bulk lines: a line with qty >= 100 has its line amount multiplied by 0.90 (before any line rounding).
- [CHANGED] Tier discount (replaces the earlier tier rates): 'platinum' 10%, 'gold' 7%, 'silver' 3%, any other tier 0%.
- [CHANGED] Validation (replaces the earlier qty rule): qty 0 is now allowed and such a line is skipped entirely; a negative qty still raises ValueError; an empty lines list or a negative unit_price still raises ValueError.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
