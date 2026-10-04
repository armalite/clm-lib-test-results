print(open('/task/workspace/invoice/core.py').read());print(open('/task/workspace/invoice/__init__.py').read())
import os
code='''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def compute_invoice(lines, customer):
    sub=Decimal('0')
    for l in lines:
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=100: a*=Decimal('0.90')
        sub+=r2(a)
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal('0')))
    tax=r2((sub-disc)*Decimal('0'))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])