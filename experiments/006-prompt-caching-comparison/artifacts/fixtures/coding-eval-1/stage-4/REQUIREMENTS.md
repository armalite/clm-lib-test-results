# Stage 4 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Tax exemption: if customer.get('tax_exempt') is True, tax is 0.00 whatever the rate.
- [NEW] Money formatting: add format_money(amount: str, currency: str) -> str. Prefix 'NZD' with 'NZ$', 'AUD' with 'A$', 'USD' with 'US$'; always 2 decimals; a negative amount puts '-' before the prefix (for example '-NZ$5.00'); any other currency raises ValueError.
- [CHANGED] Tax (replaces the flat 10% rate): the tax rate depends on customer['region']: 'NZ' 15%, 'AU' 10%, 'US' 0%, any other region 12%.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
