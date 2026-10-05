# Stage 2 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Tier discount: discount rate by customer['tier']: 'gold' 5%, 'silver' 2%, any other tier 0%.
- [CHANGED] Tax (replaces the flat 10% rate): the tax rate depends on customer['region']: 'NZ' 15%, 'AU' 10%, 'US' 0%, any other region 12%.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
