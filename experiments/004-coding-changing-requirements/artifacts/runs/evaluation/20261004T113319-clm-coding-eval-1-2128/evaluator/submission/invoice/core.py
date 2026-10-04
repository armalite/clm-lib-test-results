"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)


def _line_amount(line):
    q = line['qty']
    amt = Decimal(q) * Decimal(str(line['unit_price']))
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')
    return amt


def _discount_rate(subtotal, customer, lines):
    t = (customer or {}).get('tier')
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(t, Decimal('0'))


def _tax_rate(customer):
    c = customer or {}
    if c.get('tax_exempt') is True:
        return Decimal('0')
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(c.get('region'), Decimal('0.12'))


def _validate(lines):
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
    _validate(lines)
    subtotal = sum((_line_amount(l) for l in lines), Decimal('0'))
    discount = subtotal * _discount_rate(subtotal, customer, lines)
    tax = (subtotal - discount) * _tax_rate(customer)
    rs, rd, rt = _r(subtotal), _r(discount), _r(tax)
    total = rs - rd + rt
    return {'subtotal': str(rs), 'discount': str(rd), 'tax': str(rt), 'total': str(total)}


def format_money(amount, currency):
    pre = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}.get(currency)
    if pre is None:
        raise ValueError('bad currency')
    a = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
    sign = '-' if a < 0 else ''
    return sign + pre + str(abs(a))
