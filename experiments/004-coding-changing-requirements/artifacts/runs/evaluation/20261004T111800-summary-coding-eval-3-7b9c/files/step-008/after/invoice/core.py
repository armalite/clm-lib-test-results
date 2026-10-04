from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def _re(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)


TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}


def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))


def tax_rate(customer):
    return Decimal('0.10')


def compute_invoice(lines, customer):
    sub = sum((Decimal(l['qty']) * Decimal(l['unit_price']) * (Decimal('0.90') if l['qty'] >= 100 else 1) for l in lines), Decimal('0'))
    disc = sub * discount_rate(lines, customer, sub)
    tax = (sub - disc) * tax_rate(customer)
    if customer.get('tax_exempt') is True:
        tax = Decimal('0')
    s, d, t = _re(sub), _re(disc), _re(tax)
    total = s - d + t
    return {'subtotal': str(s), 'discount': str(d), 'tax': str(t), 'total': str(_re(total))}


PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}


def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _r(Decimal(amount))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + '{:,.2f}'.format(abs(a))
