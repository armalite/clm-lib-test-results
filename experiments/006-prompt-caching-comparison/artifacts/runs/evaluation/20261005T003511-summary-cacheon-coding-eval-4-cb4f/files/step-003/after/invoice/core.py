"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')


def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)


def tier_rate(customer):
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(customer.get('tier'), Decimal('0'))


def tax_rate(customer):
    return Decimal('0')


def line_amount(line):
    amt = Decimal(int(line['qty'])) * Decimal(str(line['unit_price']))
    if int(line['qty']) >= 100:
        amt = amt * Decimal('0.90')
    return r2(amt)


def compute_invoice(lines, customer):
    subtotal = sum((line_amount(l) for l in lines), Decimal('0.00'))
    subtotal = r2(subtotal)
    discount = r2(subtotal * tier_rate(customer))
    tax = r2((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}


def format_money(amount, currency):
    raise NotImplementedError
