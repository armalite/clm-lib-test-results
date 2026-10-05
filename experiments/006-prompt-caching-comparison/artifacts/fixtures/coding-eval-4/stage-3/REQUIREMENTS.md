# Stage 3 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Money formatting: add format_money(amount: str, currency: str) -> str. Prefix 'NZD' with 'NZ$', 'AUD' with 'A$', 'USD' with 'US$'; always 2 decimals; a negative amount puts '-' before the prefix (for example '-NZ$5.00'); any other currency raises ValueError.
- [CHANGED] Bulk lines (replaces the earlier bulk rule): qty >= 200 multiplies the line amount by 0.88; otherwise qty >= 50 multiplies it by 0.95; smaller lines are unchanged (before any line rounding).

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
