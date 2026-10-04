# Stage 4 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Bulk lines: a line with qty >= 100 has its line amount multiplied by 0.90 (before any line rounding).
- [CHANGED] Tax (replaces the flat 10% rate): the tax rate depends on customer['region']: 'NZ' 15%, 'AU' 10%, 'US' 0%, any other region 12%.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
