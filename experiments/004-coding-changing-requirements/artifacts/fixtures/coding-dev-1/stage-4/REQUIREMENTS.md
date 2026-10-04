# Stage 4 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Money formatting: add format_money(amount: str, currency: str) -> str. Prefix 'NZD' with 'NZ$', 'AUD' with 'A$', 'USD' with 'US$'; always 2 decimals; a negative amount puts '-' before the prefix (for example '-NZ$5.00'); any other currency raises ValueError.
- [CHANGED] Tier discount (replaces the earlier tier rates): 'platinum' 10%, 'gold' 7%, 'silver' 3%, any other tier 0%.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
