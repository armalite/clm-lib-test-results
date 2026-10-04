"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')
TIER = {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}


def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub = Decimal('0')
    for ln in lines:
        q = ln.get('qty')
        if not isinstance(q, int) or isinstance(q, bool) or q < 0:
            raise ValueError('bad qty')
        p = Decimal(str(ln.get('unit_price')))
        if p < 0:
            raise ValueError('negative price')
        if q == 0:
            continue
        amt = q * p
        if q >= 100:
            amt = amt * Decimal('0.90')
        sub += r2(amt)
    disc = r2(sub * TIER.get(customer.get('tier'), Decimal('0')))
    tax_rate = Decimal('0.10')
    tax = r2((sub - disc) * tax_rate)
    total = sub - disc + tax
    return {'subtotal': str(r2(sub)), 'discount': str(disc), 'tax': str(tax), 'total': str(r2(total))}


PFX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}


def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('bad currency')
    a = r2(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PFX[currency] + str(abs(a))
