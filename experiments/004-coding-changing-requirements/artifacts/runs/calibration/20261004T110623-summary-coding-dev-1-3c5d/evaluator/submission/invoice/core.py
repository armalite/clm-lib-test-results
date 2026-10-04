"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def he(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def discount_rate(subtotal, customer):
    return {'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub = Decimal('0')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        p = Decimal(str(l['unit_price']))
        if p < 0:
            raise ValueError('negative price')
        amt = q * p
        if q >= 100:
            amt = amt * Decimal('0.90')
        sub += amt
    disc = sub * discount_rate(sub, customer)
    tax = (sub - disc) * tax_rate(customer)
    rs, rd, rt = he(sub), he(disc), he(tax)
    total = rs - rd + rt
    return {'subtotal': str(rs), 'discount': str(rd), 'tax': str(rt), 'total': str(he(total))}

def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre:
        raise ValueError('unknown currency')
    d=Decimal(str(amount)).quantize(Q, rounding=ROUND_HALF_EVEN)
    sign='-' if d<0 else ''
    return sign+pre[currency]+str(abs(d))
