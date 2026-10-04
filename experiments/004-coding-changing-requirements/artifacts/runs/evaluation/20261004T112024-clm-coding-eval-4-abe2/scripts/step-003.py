code='''"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_UP

C=Decimal('0.01')
def r2(x): return x.quantize(C, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def line_amount(l):
    a=Decimal(l['qty'])*Decimal(l['unit_price'])
    if l['qty']>=100: a*=Decimal('0.90')
    return r2(a)

def discount_rate(customer, subtotal):
    return TIER.get(customer.get('tier'),Decimal(0))

def tax_rate(customer):
    return Decimal(0)

def compute_invoice(lines, customer):
    sub=sum((line_amount(l) for l in lines),Decimal(0))
    disc=r2(sub*discount_rate(customer,sub))
    tax=r2((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: invoice/core.py has r2 (half-up), line_amount (bulk qty>=100 x0.90), discount_rate(customer,subtotal) tier gold5/silver2, tax_rate(customer)=0, compute_invoice, format_money stub (NotImplemented). Tests at /task/fixtures/current-tests.'}]},open('/task/workspace/context.json','w'))