# Stage 2 of 6 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [NEW] Tier discount: a percentage discount by customer['tier']: 'gold' 5%, 'silver' 2%, any other tier 0%. The tier discount is the rate times the tier-eligible amount, which is the subtotal unless a rule says otherwise.
- [NEW] Bulk lines: a line with qty >= 100 is a bulk line; its line amount is multiplied by 0.90. This is a line adjustment, applied before any line rounding.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
