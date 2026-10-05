"""Invoice core."""
from decimal import Decimal, ROUND_HALF_EVEN

Q = Decimal('0.01')


def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)


def discount_rate(lines, customer, subtotal):
    t = (customer or {}).get('tier')
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(t, Decimal('0'))


def tax_rate(customer):
    c = customer or {}
    if c.get('tax_exempt') is True:
        return Decimal('0')
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(c.get('region'), Decimal('0.12'))


def line_amount(line):
    q = int(line['qty'])
    amt = Decimal(q) * Decimal(str(line['unit_price']))
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
    disc = subtotal * discount_rate(lines, customer, subtotal)
    tax = (subtotal - disc) * tax_rate(customer)
    subtotal, discount, tax = r2(subtotal), r2(disc), r2(tax)
    total = subtotal - discount + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}


def format_money(amount, currency):
    pre = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}
    if currency not in pre:
        raise ValueError('unsupported currency: %r' % (currency,))
    a = r2(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return '%s%s%s' % (sign, pre[currency], format(abs(a), '.2f'))
