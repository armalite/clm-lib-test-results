from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal("0.01")


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def _re(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)


TIER = {"gold": Decimal("0.05"), "silver": Decimal("0.02")}


def discount_rate(lines, customer, subtotal):
    return TIER.get((customer or {}).get("tier"), Decimal(0))


def tax_rate(customer):
    return {"NZ": Decimal("0.15"), "AU": Decimal("0.10"), "US": Decimal(0)}.get((customer or {}).get("region"), Decimal("0.12"))


def compute_invoice(lines, customer):
    customer = customer or {}
    if not lines:
        raise ValueError("empty")
    sub = Decimal(0)
    for l in lines:
        q = l.get("qty")
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError("qty")
        up = Decimal(str(l["unit_price"]))
        if up < 0:
            raise ValueError("price")
        f = Decimal("0.88") if q >= 200 else Decimal("0.95") if q >= 50 else Decimal(1)
        sub += q * up * f
    disc = sub * discount_rate(lines, customer, sub)
    tax = (sub - disc) * tax_rate(customer)
    if customer.get("tax_exempt") is True:
        tax = Decimal(0)
    s, d, t = _re(sub), _re(disc), _re(tax)
    return {"subtotal": str(s), "discount": str(d), "tax": str(t), "total": str(s - d + t)}


PREFIX = {"NZD": "NZ$", "AUD": "A$", "USD": "US$"}


def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _r(Decimal(str(amount)))
    sign = "-" if a < 0 else ""
    return f"{sign}{PREFIX[currency]}{abs(a):,.2f}"
