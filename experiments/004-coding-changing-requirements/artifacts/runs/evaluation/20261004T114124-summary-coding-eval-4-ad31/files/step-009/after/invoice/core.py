"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER = {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}

def line_amount(line):
    amt = Decimal(int(line['qty'])) * Decimal(str(line['unit_price']))
    q = int(line['qty'])
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')
    return amt

def discount_rate(customer):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q < 0:
            raise ValueError('bad qty')
        try:
            up = Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('bad price')
        if not up.is_finite() or up < 0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
    from decimal import ROUND_HALF_EVEN
    he = lambda x: x.quantize(Q, rounding=ROUND_HALF_EVEN)
    ex = sum((line_amount(l) for l in lines if l['qty'] != 0), Decimal('0'))
    dex = ex * discount_rate(customer)
    tex = Decimal('0') if customer.get('tax_exempt') is True else (ex - dex) * tax_rate(customer)
    subtotal, discount, tax = he(ex), he(dex), he(tex)
    total = subtotal - discount + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}

PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a = r2(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + str(abs(a))
