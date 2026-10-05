"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_EVEN

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def line_amount(line):
    q = int(line['qty'])
    amt = Decimal(q) * Decimal(str(line['unit_price']))
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')
    return amt

def discount_rate(subtotal, customer):
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if p < 0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
    sub = sum((line_amount(l) for l in lines), Decimal('0'))
    disc = sub * discount_rate(sub, customer)
    tax = (sub - disc) * tax_rate(customer)
    rs, rd, rt = r2(sub), r2(disc), r2(tax)
    total = rs - rd + rt
    return {'subtotal': str(rs), 'discount': str(rd), 'tax': str(rt), 'total': str(r2(total))}

def format_money(amount, currency):
    raise NotImplementedError
