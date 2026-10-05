src='''"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')


def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)


def line_amount(line, customer):
    amt = Decimal(line['qty']) * Decimal(line['unit_price'])
    if line['qty'] >= 100:
        amt = amt * Decimal('0.90')
    return r2(amt)


def discount_rate(subtotal, lines, customer):
    return Decimal('0')


def tax_rate(customer):
    return Decimal('0.10')


def compute_invoice(lines, customer):
    subtotal = sum((line_amount(l, customer) for l in lines), Decimal('0'))
    subtotal = r2(subtotal)
    discount = r2(subtotal * discount_rate(subtotal, lines, customer))
    tax = r2((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
import json
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done in invoice/core.py: line_amount (bulk qty>=100 x0.90, round half up), discount_rate()=0, tax_rate()=0.10, compute_invoice returns 2dp strings. format_money stub (NotImplemented). Tests: unittest discover -s /task/fixtures/current-tests cwd /task/workspace.'}]},open('/task/workspace/context.json','w'))
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])