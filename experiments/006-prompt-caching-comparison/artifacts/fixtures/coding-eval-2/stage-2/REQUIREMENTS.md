# Stage 2 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Tax: the tax rate is 10% for every customer.
- [NEW] Money formatting: add format_money(amount: str, currency: str) -> str. Prefix 'NZD' with 'NZ$', 'AUD' with 'A$', 'USD' with 'US$'; always 2 decimals; a negative amount puts '-' before the prefix (for example '-NZ$5.00'); any other currency raises ValueError.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
