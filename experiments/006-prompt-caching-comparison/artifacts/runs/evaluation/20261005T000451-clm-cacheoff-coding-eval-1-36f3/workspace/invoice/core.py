"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')


def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)


def line_amount(line, customer):
    amt = Decimal(line['qty']) * Decimal(str(line['unit_price']))
    if line['qty'] >= 200:
        amt = amt * Decimal('0.88')
    elif line['qty'] >= 50:
        amt = amt * Decimal('0.95')
    return amt


def discount_rate(subtotal, lines, customer):
    tier = (customer or {}).get('tier')
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(tier, Decimal('0'))


def tax_rate(customer=None):
    c = customer or {}
    if c.get('tax_exempt') is True:
        return Decimal('0')
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(c.get('region'), Decimal('0.12'))


def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price'))) < 0:
            raise ValueError('negative price')


def he(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)


def compute_invoice(lines, customer):
    validate(lines)
    sub = sum((line_amount(l, customer) for l in lines), Decimal('0'))
    disc = sub * discount_rate(sub, lines, customer)
    tax = (sub - disc) * tax_rate(customer)
    rs, rd, rt = he(sub), he(disc), he(tax)
    total = rs - rd + rt
    return {'subtotal': str(rs), 'discount': str(rd), 'tax': str(rt), 'total': str(total.quantize(Q))}


def format_money(amount, currency):
    pre = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}.get(currency)
    if pre is None:
        raise ValueError('unknown currency')
    a = Decimal(str(amount)).quantize(Q, rounding=ROUND_HALF_UP)
    sign = '-' if a < 0 else ''
    return sign + pre + str(abs(a))
