code='''from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(lines, customer, subtotal):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    subtotal = sum((_r(Decimal(l['qty']) * Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    discount = _r(subtotal * discount_rate(lines, customer, subtotal))
    tax = _r((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {k: str(_r(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}

PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _r(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 implemented in invoice/core.py: _r half-up, discount_rate(lines,customer,subtotal)=0, tax_rate(customer)=0.10, format_money with PREFIX dict (NZ$,A$,US$), neg sign before prefix, ValueError otherwise.'}]},open('/task/workspace/context.json','w'))