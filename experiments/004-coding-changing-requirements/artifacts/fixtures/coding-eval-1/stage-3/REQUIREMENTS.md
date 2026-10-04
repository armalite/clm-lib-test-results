# Stage 3 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Tier discount: discount rate by customer['tier']: 'gold' 5%, 'silver' 2%, any other tier 0%.
- [CHANGED] Rounding (replaces the earlier rounding rule): do NOT round line amounts. Compute the subtotal, discount and tax exactly (discount from the exact subtotal; tax from the exact subtotal minus the exact discount), then round each of subtotal, discount and tax to 2 decimals using banker's rounding (half even); total = rounded subtotal - rounded discount + rounded tax.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
