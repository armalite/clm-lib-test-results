"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def _e(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)


def _discount_rate(lines, customer, subtotal):
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(customer.get('tier'), Decimal('0'))


def _tax_rate(customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return Decimal('0.10')


def compute_invoice(lines, customer):
    sub = sum(((int(l['qty']) * Decimal(str(l['unit_price'])) * (Decimal('0.90') if int(l['qty'])>=100 else 1)) for l in lines), Decimal('0'))
    disc = sub * _discount_rate(lines, customer, sub)
    tax = (sub - disc) * _tax_rate(customer)
    s, d, t = _e(sub), _e(disc), _e(tax)
    total = s - d + t
    return {'subtotal': str(s), 'discount': str(d), 'tax': str(t), 'total': str(_e(total))}


PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}


def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _r(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + '{:,.2f}'.format(abs(a))
