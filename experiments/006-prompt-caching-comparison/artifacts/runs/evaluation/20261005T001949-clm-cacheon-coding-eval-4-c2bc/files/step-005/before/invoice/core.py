"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}

def line_amount(line):
    a = Decimal(line['qty']) * Decimal(str(line['unit_price']))
    if line['qty'] >= 100:
        a = a * Decimal('0.90')
    return r2(a)

def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(lines, customer):
    return Decimal('0')

def compute_invoice(lines, customer):
    sub = sum((line_amount(l) for l in lines), Decimal('0'))
    sub = r2(sub)
    disc = r2(sub * discount_rate(lines, customer, sub))
    tax = r2((sub - disc) * tax_rate(lines, customer))
    total = sub - disc + tax
    return {k: str(r2(v)) for k, v in (('subtotal', sub), ('discount', disc), ('tax', tax), ('total', total))}

def format_money(amount, currency):
    raise NotImplementedError
