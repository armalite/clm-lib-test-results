# Stage 6 of 6 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [CHANGED] Rounding (replaces the whole rounding rule from stage 1): do not round line amounts or any intermediate value; all calculations and comparisons use exact values. Only at the end, round subtotal, discount and tax each to 2 decimals using half-even (banker's) rounding; total = rounded subtotal - rounded discount + shipping + rounded tax.
- [CHANGED] Shipping (partly replaces the stage-3 rule): shipping is now taxed, so the tax is computed on (subtotal - discount + shipping). The 7.50 fee and the 100.00 threshold are unchanged.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
