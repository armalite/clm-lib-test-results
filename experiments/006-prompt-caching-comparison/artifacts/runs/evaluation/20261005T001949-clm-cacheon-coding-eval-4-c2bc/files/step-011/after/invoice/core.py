"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER = {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}

def line_amount(line):
    a = Decimal(line['qty']) * Decimal(str(line['unit_price']))
    if line['qty'] >= 200:
        a = a * Decimal('0.88')
    elif line['qty'] >= 50:
        a = a * Decimal('0.95')
    return a

def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(lines, customer):
    return Decimal('0.10')

def validate(lines):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q < 0:
            raise ValueError('qty')
        if Decimal(str(l.get('unit_price'))) < 0:
            raise ValueError('price')

def re2(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    validate(lines)
    act = [l for l in lines if l['qty'] != 0]
    sub = sum((line_amount(l) for l in act), Decimal('0'))
    disc = sub * discount_rate(act, customer, sub)
    if customer.get('tax_exempt') is True:
        tax = Decimal('0')
    else:
        tax = (sub - disc) * tax_rate(act, customer)
    sub, disc, tax = re2(sub), re2(disc), re2(tax)
    total = sub - disc + tax
    return {k: str(re2(v)) for k, v in (('subtotal', sub), ('discount', disc), ('tax', tax), ('total', total))}

PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('currency')
    d = r2(Decimal(str(amount)))
    sign = '-' if d < 0 else ''
    return sign + PREFIX[currency] + str(abs(d))
