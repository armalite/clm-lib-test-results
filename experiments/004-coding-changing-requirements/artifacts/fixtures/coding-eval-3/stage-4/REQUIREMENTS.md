# Stage 4 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Validation: compute_invoice raises ValueError if lines is empty, if any qty is not a positive integer, or if any unit_price is negative.
- [CHANGED] Tax (replaces the flat 10% rate): the tax rate depends on customer['region']: 'NZ' 15%, 'AU' 10%, 'US' 0%, any other region 12%.
- [CHANGED] Bulk lines (replaces the earlier bulk rule): qty >= 200 multiplies the line amount by 0.88; otherwise qty >= 50 multiplies it by 0.95; smaller lines are unchanged (before any line rounding).

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
