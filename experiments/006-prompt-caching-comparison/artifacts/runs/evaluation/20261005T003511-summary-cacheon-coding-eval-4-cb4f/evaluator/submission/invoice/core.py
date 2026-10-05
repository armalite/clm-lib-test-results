"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')


def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)


def tier_rate(customer):
    return {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}.get(customer.get('tier'), Decimal('0'))


def tax_rate(customer):
    return Decimal('0.10')


def line_amount(line):
    amt = Decimal(int(line['qty'])) * Decimal(str(line['unit_price']))
    q = int(line['qty'])
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')
    return amt


def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if not isinstance(q, int) or isinstance(q, bool) or q < 0:
            raise ValueError('bad qty')
        try:
            up = Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if not up.is_finite() or up < 0:
            raise ValueError('negative price')


def re2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)


def compute_invoice(lines, customer):
    validate(lines)
    sub = sum((line_amount(l) for l in lines if l['qty'] != 0), Decimal('0'))
    disc = sub * tier_rate(customer)
    if customer.get('tax_exempt') is True:
        tax = Decimal('0')
    else:
        tax = (sub - disc) * tax_rate(customer)
    s_, d_, t_ = re2(sub), re2(disc), re2(tax)
    total = s_ - d_ + t_
    return {'subtotal': str(s_), 'discount': str(d_), 'tax': str(t_), 'total': str(re2(total))}


_PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}


def format_money(amount, currency):
    if currency not in _PREFIX:
        raise ValueError('unknown currency')
    d = r2(Decimal(str(amount)))
    sign = '-' if d < 0 else ''
    return sign + _PREFIX[currency] + str(abs(d))
