code='''"""Invoice core."""
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
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: invoice/core.py has r2(), line_amount (bulk>=100 x0.90), discount_rate(lines,customer,sub) tier gold5/silver2, tax_rate()=0, compute_invoice, format_money stub (NotImplemented). Run tests via unittest discover -s /task/fixtures/current-tests.'}]},open('/task/workspace/context.json','w'))