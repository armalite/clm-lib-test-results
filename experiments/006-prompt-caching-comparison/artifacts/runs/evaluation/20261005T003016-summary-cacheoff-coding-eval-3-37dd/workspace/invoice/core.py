from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal("0.01")


def _r(x, mode=ROUND_HALF_EVEN):
    return x.quantize(Q, rounding=mode)


def discount_rate(subtotal, customer):
    return {"gold": Decimal("0.05"), "silver": Decimal("0.02")}.get(customer.get("tier"), Decimal("0"))


def tax_rate(customer):
    return {"NZ": Decimal("0.15"), "AU": Decimal("0.10"), "US": Decimal("0")}.get(customer.get("region"), Decimal("0.12"))


def _line(l):
    q = int(l["qty"])
    a = q * Decimal(str(l["unit_price"]))
    if q >= 200:
        a = a * Decimal("0.88")
    elif q >= 50:
        a = a * Decimal("0.95")
    return a


def _validate(lines):
    if not lines:
        raise ValueError("empty lines")
    for l in lines:
        q = l.get("qty")
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError("bad qty")
        try:
            u = Decimal(str(l["unit_price"]))
        except Exception:
            raise ValueError("bad unit_price")
        if not u.is_finite() or u < 0:
            raise ValueError("negative unit_price")


def compute_invoice(lines, customer):
    _validate(lines)
    sub = sum((_line(l) for l in lines), Decimal("0"))
    disc = sub * discount_rate(sub, customer)
    tax = (sub - disc) * tax_rate(customer)
    if customer.get("tax_exempt") is True:
        tax = Decimal("0")
    s, d, t = _r(sub), _r(disc), _r(tax)
    total = s - d + t
    return {"subtotal": str(s), "discount": str(d), "tax": str(t), "total": str(_r(total))}


PREFIX = {"NZD": "NZ$", "AUD": "A$", "USD": "US$"}


def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _r(Decimal(str(amount)), ROUND_HALF_UP)
    sign = "-" if a < 0 else ""
    return f"{sign}{PREFIX[currency]}{abs(a):,.2f}"
