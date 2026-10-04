# Stage 7 of 8 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [NEW] Coupons: customer may contain 'coupon', a decimal string such as '15.00' (a missing coupon means 0). The coupon is applied after the tier discount, and only up to the amount left: coupon applied = min(coupon, subtotal - tier discount). discount = tier discount + coupon applied.
- [CHANGED] Shipping (partly replaces the stage-2 rule): shipping is now taxed, so the tax is computed on (subtotal - discount + shipping). The 7.50 fee and the 100.00 threshold are unchanged.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
