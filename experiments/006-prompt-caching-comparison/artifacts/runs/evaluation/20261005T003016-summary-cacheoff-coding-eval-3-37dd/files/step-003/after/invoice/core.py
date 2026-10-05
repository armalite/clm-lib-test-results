from decimal import Decimal, ROUND_HALF_UP

Q = Decimal("0.01")


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def discount_rate(subtotal, customer):
    return Decimal("0")


def tax_rate(customer):
    return Decimal("0.10")


def compute_invoice(lines, customer):
    subtotal = sum((_r(int(l["qty"]) * Decimal(str(l["unit_price"]))) for l in lines), Decimal("0"))
    subtotal = _r(subtotal)
    discount = _r(subtotal * discount_rate(subtotal, customer))
    tax = _r((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {"subtotal": str(subtotal), "discount": str(discount), "tax": str(tax), "total": str(_r(total))}


PREFIX = {"NZD": "NZ$", "AUD": "A$", "USD": "US$"}


def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _r(Decimal(str(amount)))
    sign = "-" if a < 0 else ""
    return f"{sign}{PREFIX[currency]}{abs(a)}"
