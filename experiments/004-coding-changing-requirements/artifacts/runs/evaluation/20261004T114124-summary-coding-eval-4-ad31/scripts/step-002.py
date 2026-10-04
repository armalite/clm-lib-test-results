code='''\"\"\"Invoice core.\"\"\"
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}

def line_amount(line):
    amt = Decimal(int(line['qty'])) * Decimal(str(line['unit_price']))
    if int(line['qty']) >= 100:
        amt = amt * Decimal('0.90')
    return r2(amt)

def discount_rate(customer):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0')

def compute_invoice(lines, customer):
    subtotal = sum((line_amount(l) for l in lines), Decimal('0'))
    discount = r2(subtotal * discount_rate(customer))
    tax = r2((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','w').write('Stage1 done: rounding half-up per line, bulk qty>=100 x0.90, tier gold5 silver2. core.py has line_amount/discount_rate/tax_rate hooks.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])