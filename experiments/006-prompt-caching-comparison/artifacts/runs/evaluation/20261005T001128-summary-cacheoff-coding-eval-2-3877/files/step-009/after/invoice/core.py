from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER_RATES = {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}
BULK_QTY = 100
BULK_FACTOR = Decimal('0.90')

def discount_rate(customer, subtotal):
    return TIER_RATES.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if not isinstance(q, int) or isinstance(q, bool) or q < 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(l.get('unit_price')))
        except (InvalidOperation, ValueError, TypeError):
            raise ValueError('bad price')
        if not p.is_finite() or p < 0:
            raise ValueError('negative price')

def line_amount(l):
    q = l['qty']
    amt = Decimal(q) * Decimal(str(l['unit_price']))
    if q >= BULK_QTY:
        amt = amt * BULK_FACTOR
    return r2(amt)

def compute_invoice(lines, customer):
    _validate(lines)
    subtotal = sum((line_amount(l) for l in lines if l['qty'] != 0), Decimal('0'))
    subtotal = r2(subtotal)
    discount = r2(subtotal * discount_rate(customer, subtotal))
    tax = r2((subtotal - discount) * tax_rate(customer))
    if customer.get('tax_exempt') is True:
        tax = Decimal('0.00')
    total = subtotal - discount + tax
    return {'subtotal': str(subtotal), 'discount': str(discount), 'tax': str(tax), 'total': str(r2(total))}

PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a = r2(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + '{:,.2f}'.format(abs(a))
