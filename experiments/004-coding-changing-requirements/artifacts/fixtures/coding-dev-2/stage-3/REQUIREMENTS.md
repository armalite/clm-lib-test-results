# Stage 3 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Validation: compute_invoice raises ValueError if lines is empty, if any qty is not a positive integer, or if any unit_price is negative.
- [NEW] Tax exemption: if customer.get('tax_exempt') is True, tax is 0.00 whatever the rate.
- [CHANGED] Tier discount (replaces the earlier tier rates): 'platinum' 10%, 'gold' 7%, 'silver' 3%, any other tier 0%.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
