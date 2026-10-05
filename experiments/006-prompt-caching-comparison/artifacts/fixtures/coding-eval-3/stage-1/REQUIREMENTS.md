# Stage 1 of 4 requirements

## Package and API

Implement the package `invoice` in /task/workspace/invoice/ (a starting skeleton is provided).
Standard library only. Use `decimal.Decimal` arithmetic.

- `invoice.compute_invoice(lines, customer) -> dict`
  - `lines`: list of `{"sku": str, "qty": int, "unit_price": str}`. unit_price is a decimal
    string such as "12.50"; it may have more than 2 decimal places (for example "3.125").
  - `customer`: `{"tier": str, "region": str}` and optionally `"tax_exempt": bool`.
  - Returns `{"subtotal": str, "discount": str, "tax": str, "total": str}`, each a string with
    exactly 2 decimals, for example "12.30".
- Base calculation (always in force): line amount = qty x unit_price; subtotal = sum of line
  amounts; discount = subtotal x discount rate; tax = (subtotal - discount) x tax rate;
  total = subtotal - discount + tax. With no discount rule in force the discount rate is 0; with
  no tax rule in force the tax rate is 0.

## Rules introduced in stage 1

- [NEW] Rounding: round each line amount to 2 decimals (half up) before summing; compute discount from the rounded subtotal and round it to 2 decimals (half up); compute tax from (subtotal - discount) and round it to 2 decimals (half up); total = subtotal - discount + tax.
- [NEW] Tax: the tax rate is 10% for every customer.
- [NEW] Money formatting: add format_money(amount: str, currency: str) -> str. Prefix 'NZD' with 'NZ$', 'AUD' with 'A$', 'USD' with 'US$'; always 2 decimals; a negative amount puts '-' before the prefix (for example '-NZ$5.00'); any other currency raises ValueError.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
