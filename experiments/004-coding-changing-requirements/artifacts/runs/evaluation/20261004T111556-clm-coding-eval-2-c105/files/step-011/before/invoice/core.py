"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')
TIER_RATES = {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}


def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def discount_rate(customer, subtotal):
    return TIER_RATES.get(customer.get('tier'), Decimal('0'))


def tax_rate(customer):
    return Decimal('0.10')


def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    subtotal = Decimal('0')
    for ln in lines:
        q = ln.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q < 0:
            raise ValueError('bad qty')
        p = Decimal(str(ln.get('unit_price')))
        if p < 0:
            raise ValueError('negative price')
        if q == 0:
            continue
        amt = q * p
        if q >= 100:
            amt = amt * Decimal('0.90')
        subtotal += r2(amt)
    disc = r2(subtotal * discount_rate(customer, subtotal))
    tax = r2((subtotal - disc) * tax_rate(customer))
    total = subtotal - disc + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', disc), ('tax', tax), ('total', total))}


PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}


def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a = r2(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + str(abs(a))
