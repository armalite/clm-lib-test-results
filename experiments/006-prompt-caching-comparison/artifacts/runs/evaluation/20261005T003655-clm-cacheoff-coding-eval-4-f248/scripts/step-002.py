code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    sub=Decimal('0')
    for l in lines:
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=100:
            a*=Decimal('0.90')
        sub+=_r(a)
    disc=_r(sub*TIER.get(customer.get('tier'),Decimal('0')))
    tax=_r((sub-disc)*Decimal('0'))
    tot=sub-disc+tax
    return {k:str(_r(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
import json
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done in invoice/core.py: compute_invoice with _r half-up, bulk qty>=100 x0.90, TIER dict gold .05 silver .02, tax rate 0 placeholder. format_money unimplemented.'}]},open('/task/workspace/context.json','w'))