"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def re2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

def discount_rate(lines, customer, subtotal):
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(customer.get('region'), Decimal('0.12'))

def bulk(q):
    if q >= 200:
        return Decimal('0.88')
    if q >= 50:
        return Decimal('0.95')
    return Decimal('1')

def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('bad price')
        if not p.is_finite() or p < 0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
    sub = sum((Decimal(l['qty']) * Decimal(l['unit_price']) * bulk(l['qty']) for l in lines), Decimal('0'))
    disc = sub * discount_rate(lines, customer, sub)
    tax = (sub - disc) * tax_rate(customer)
    s, d, t = re2(sub), re2(disc), re2(tax)
    total = s - d + t
    return {'subtotal': str(s), 'discount': str(d), 'tax': str(t), 'total': str(re2(total))}

PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = r2(Decimal(amount))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + '{:,.2f}'.format(abs(a))
