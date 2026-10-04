# Stage 7 of 8 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [NEW] Coupons: customer may contain 'coupon', a decimal string such as '15.00' (a missing coupon means 0). The coupon is applied after the tier discount, and only up to the amount left: coupon applied = min(coupon, subtotal - tier discount). discount = tier discount + coupon applied.
- [CHANGED] Bulk lines (partly replaces the stage-2 rule): a line is now a bulk line when qty >= 50. The 0.90 multiplier and everything else about bulk lines are unchanged.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
