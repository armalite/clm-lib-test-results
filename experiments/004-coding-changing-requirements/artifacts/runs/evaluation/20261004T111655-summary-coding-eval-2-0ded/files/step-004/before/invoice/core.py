"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')
TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}


def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub = Decimal('0')
    for ln in lines:
        q = ln.get('qty')
        if not isinstance(q, int) or isinstance(q, bool) or q <= 0:
            raise ValueError('bad qty')
        p = Decimal(str(ln.get('unit_price')))
        if p < 0:
            raise ValueError('negative price')
        sub += r2(q * p)
    disc = r2(sub * TIER.get(customer.get('tier'), Decimal('0')))
    tax_rate = Decimal('0')
    tax = r2((sub - disc) * tax_rate)
    total = sub - disc + tax
    return {'subtotal': str(r2(sub)), 'discount': str(disc), 'tax': str(tax), 'total': str(r2(total))}


def format_money(amount, currency):
    raise NotImplementedError
