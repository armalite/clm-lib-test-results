# Stage 3 of 6 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [NEW] Bulk lines: a line with qty >= 100 is a bulk line; its line amount is multiplied by 0.90. This is a line adjustment, applied before any line rounding.
- [NEW] Tax: the tax rate is 10% for every customer.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
