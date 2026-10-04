# Stage 8 of 8 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [NEW] Refunds: add invoice.compute_refund(lines, customer, returns) -> str. returns maps a sku to the number of units returned. Compute the original invoice and an invoice for the kept quantities (qty minus returned; lines with nothing kept are left out) with every rule in force for compute_invoice, except that shipping is 0.00 in both. The refund is the original total minus the kept total, where the kept total is 0.00 if no line is kept; a negative difference gives a refund of 0.00. Return it as a string with exactly 2 decimals. Raise ValueError if a returned sku is not in lines or a returned quantity is not an integer between 1 and that line's qty.
- [CHANGED] Rounding (replaces the whole rounding rule from stage 1): do not round line amounts or any intermediate value; all calculations and comparisons use exact values. Only at the end, round subtotal, discount and tax each to 2 decimals using half-even (banker's) rounding; total = rounded subtotal - rounded discount + shipping + rounded tax.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
