# Stage 2 of 4 requirements

Only the changes are listed. Every earlier requirement that is not replaced below remains in force.

## Changes

- [NEW] Tax: the tax rate is 10% for every customer.
- [CHANGED] Money formatting (replaces the earlier format): format_money also uses comma thousands separators, for example format_money('1234.5', 'NZD') == 'NZ$1,234.50'. Prefixes, the minus sign position and unknown-currency errors are unchanged.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
