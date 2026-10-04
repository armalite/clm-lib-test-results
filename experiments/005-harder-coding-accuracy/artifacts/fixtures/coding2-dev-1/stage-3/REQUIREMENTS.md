# Stage 3 of 6 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [NEW] Shipping: shipping is 7.50 when subtotal - discount is below 100.00, otherwise 0.00. Shipping is not taxed and not discounted.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
