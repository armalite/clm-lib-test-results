"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER_RATES = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}

def _validate(lines):
    if not lines:
        raise ValueError('lines empty')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price'))) < 0:
            raise ValueError('negative price')

def discount_rate(lines, customer, subtotal):
    return TIER_RATES.get(customer.get('tier'), Decimal('0'))

def tax_rate(lines, customer):
    return Decimal('0')

def compute_invoice(lines, customer):
    _validate(lines)
    subtotal = sum((_r(l['qty'] * Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    discount = _r(subtotal * discount_rate(lines, customer, subtotal))
    tax = _r((subtotal - discount) * tax_rate(lines, customer))
    total = subtotal - discount + tax
    return {k: str(_r(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}

def format_money(amount, currency):
    raise NotImplementedError
