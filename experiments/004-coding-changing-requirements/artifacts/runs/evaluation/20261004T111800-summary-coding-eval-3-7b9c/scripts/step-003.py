src='''from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def discount_rate(lines, customer, subtotal):
    return Decimal('0')


def tax_rate(customer):
    return Decimal('0.10')


def compute_invoice(lines, customer):
    subtotal = sum((_r(Decimal(l['qty']) * Decimal(l['unit_price'])) for l in lines), Decimal('0'))
    subtotal = _r(subtotal)
    discount = _r(subtotal * discount_rate(lines, customer, subtotal))
    tax = _r((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {k: str(_r(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}


PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}


def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _r(Decimal(amount))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','w').write('stage1 done: rounding half-up per line, tax 10%, format_money NZD/AUD/USD prefixes, neg sign before prefix.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])