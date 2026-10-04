# Stage 1 of 8 requirements

## Package and API

Implement the package `invoice` in /task/workspace/invoice/ (a starting skeleton is provided).
Standard library only. Use `decimal.Decimal` arithmetic, never float.

- `invoice.compute_invoice(lines, customer) -> dict`
  - `lines`: list of `{"sku": str, "qty": int, "unit_price": str}`. unit_price is a decimal
    string such as "12.50"; it may have more than 2 decimal places (for example "3.125").
    skus are unique within a list.
  - `customer`: a dict with `"tier": str` and `"region": str`; later stages may add optional
    fields.
  - Returns a dict with exactly the keys "subtotal", "discount", "shipping", "tax" and "total".
    Each value is a str with exactly 2 decimals, for example "12.30" or "0.00".
- Base calculation (in force unless a rule changes it): line amount = qty x unit_price;
  subtotal = sum of line amounts; discount = sum of the discounts in force (0 if none);
  shipping = 0 unless a shipping rule is in force; tax = (subtotal - discount) x tax rate (rate 0
  if no tax rule is in force); total = subtotal - discount + shipping + tax.

## Rules introduced in stage 1

- [NEW] Rounding: round each line amount to 2 decimals (half up) after any line adjustment; the subtotal is the sum of the rounded line amounts. Round every discount component and the tax to 2 decimals (half up) as soon as each is computed, and compute later values from the rounded ones.
- [NEW] Tier discount: a percentage discount by customer['tier']: 'gold' 5%, 'silver' 2%, any other tier 0%. The tier discount is the rate times the tier-eligible amount, which is the subtotal unless a rule says otherwise.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
