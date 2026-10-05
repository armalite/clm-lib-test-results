"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER_RATES = {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}

def _validate(lines):
    if not lines:
        raise ValueError('lines empty')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q < 0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price'))) < 0:
            raise ValueError('negative price')

def discount_rate(lines, customer, subtotal):
    return TIER_RATES.get(customer.get('tier'), Decimal('0'))

def tax_rate(lines, customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return Decimal('0.10')

def _amt(l):
    a = l['qty'] * Decimal(str(l['unit_price']))
    if l['qty'] >= 100:
        a = a * Decimal('0.90')
    return a

def compute_invoice(lines, customer):
    _validate(lines)
    subtotal = sum((_r(_amt(l)) for l in lines if l['qty'] != 0), Decimal('0'))
    discount = _r(subtotal * discount_rate(lines, customer, subtotal))
    tax = _r((subtotal - discount) * tax_rate(lines, customer))
    total = subtotal - discount + tax
    return {k: str(_r(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}

PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a = _r(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + '{:,.2f}'.format(abs(a))
