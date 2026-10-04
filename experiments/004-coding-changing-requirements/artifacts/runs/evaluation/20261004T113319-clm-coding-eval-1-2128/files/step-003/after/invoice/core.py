"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def _line_amount(line):
    amt = Decimal(int(line['qty'])) * Decimal(str(line['unit_price']))
    if int(line['qty']) >= 100:
        amt = amt * Decimal('0.90')
    return _r(amt)


def _discount_rate(subtotal, customer, lines):
    return Decimal('0')


def _tax_rate(customer):
    return Decimal('0.10')


def compute_invoice(lines, customer):
    subtotal = sum((_line_amount(l) for l in lines), Decimal('0'))
    discount = _r(subtotal * _discount_rate(subtotal, customer, lines))
    tax = _r((subtotal - discount) * _tax_rate(customer))
    total = subtotal - discount + tax
    return {'subtotal': str(_r(subtotal)), 'discount': str(discount), 'tax': str(tax), 'total': str(_r(total))}


def format_money(amount, currency):
    raise NotImplementedError
