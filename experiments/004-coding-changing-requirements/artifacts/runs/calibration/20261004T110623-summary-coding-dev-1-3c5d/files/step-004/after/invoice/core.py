"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(subtotal, customer):
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal('0'))

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
        sub += r2(q * p)
    disc = r2(sub * discount_rate(sub, customer))
    tax = r2((sub - disc) * tax_rate(customer))
    total = sub - disc + tax
    return {'subtotal': str(r2(sub)), 'discount': str(disc), 'tax': str(tax), 'total': str(r2(total))}

def format_money(amount, currency):
    raise NotImplementedError
