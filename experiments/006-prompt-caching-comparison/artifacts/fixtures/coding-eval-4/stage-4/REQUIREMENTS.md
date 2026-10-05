# Stage 4 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Tax exemption: if customer.get('tax_exempt') is True, tax is 0.00 whatever the rate.
- [CHANGED] Rounding (replaces the earlier rounding rule): do NOT round line amounts. Compute the subtotal, discount and tax exactly (discount from the exact subtotal; tax from the exact subtotal minus the exact discount), then round each of subtotal, discount and tax to 2 decimals using banker's rounding (half even); total = rounded subtotal - rounded discount + rounded tax.
- [CHANGED] Validation (replaces the earlier qty rule): qty 0 is now allowed and such a line is skipped entirely; a negative qty still raises ValueError; an empty lines list or a negative unit_price still raises ValueError.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
