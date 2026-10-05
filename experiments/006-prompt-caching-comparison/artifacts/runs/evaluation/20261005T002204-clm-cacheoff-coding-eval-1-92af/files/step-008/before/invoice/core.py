"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')


def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)


def discount_rate(lines, customer, subtotal):
    return Decimal('0')


def tax_rate(customer):
    return Decimal('0.10')


def line_amount(line):
    q = int(line['qty'])
    amt = Decimal(q) * Decimal(str(line['unit_price']))
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')
    return r2(amt)


def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            up = Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if not up.is_finite() or up < 0:
            raise ValueError('negative price')


def compute_invoice(lines, customer):
    validate(lines)
    subtotal = sum((line_amount(l) for l in lines), Decimal('0.00'))
    discount = r2(subtotal * discount_rate(lines, customer, subtotal))
    tax = r2((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}


def format_money(amount, currency):
    raise NotImplementedError
