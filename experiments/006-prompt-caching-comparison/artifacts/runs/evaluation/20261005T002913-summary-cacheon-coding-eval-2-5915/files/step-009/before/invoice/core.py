"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal("0.01")


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def _discount_rate(customer):
    return {"platinum": Decimal("0.10"), "gold": Decimal("0.07"), "silver": Decimal("0.03")}.get(customer.get("tier"), Decimal(0))


def _tax_rate(customer):
    return Decimal("0.10")


def compute_invoice(lines, customer):
    if not lines:
        raise ValueError("empty lines")
    sub = Decimal(0)
    for l in lines:
        q = l.get("qty")
        if not isinstance(q, int) or isinstance(q, bool) or q < 0:
            raise ValueError("bad qty")
        p = Decimal(str(l.get("unit_price")))
        if p < 0:
            raise ValueError("negative price")
        if q == 0:
            continue
        amt = q * p
        if q >= 100:
            amt = amt * Decimal("0.90")
        sub += _r(amt)
    disc = _r(sub * _discount_rate(customer))
    tax = _r((sub - disc) * _tax_rate(customer))
    total = sub - disc + tax
    return {k: str(_r(v)) for k, v in (("subtotal", sub), ("discount", disc), ("tax", tax), ("total", total))}


_PFX = {"NZD": "NZ$", "AUD": "A$", "USD": "US$"}


def format_money(amount, currency):
    if currency not in _PFX:
        raise ValueError("unknown currency")
    a = _r(Decimal(str(amount)))
    sign = "-" if a < 0 else ""
    return sign + _PFX[currency] + str(abs(a))
