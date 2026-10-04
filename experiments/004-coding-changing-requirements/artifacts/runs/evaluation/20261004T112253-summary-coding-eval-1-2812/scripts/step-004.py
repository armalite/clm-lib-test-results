code='''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
def bulk(q):
    if q>=200: return Decimal('0.88')
    if q>=50: return Decimal('0.95')
    return Decimal('1')
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('negative price')
        a=Decimal(q)*p*bulk(q)
        sub+=r2(a)
    sub=r2(sub)
    disc=r2(sub*Decimal('0'))
    tax=r2((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('S2: validation (empty, qty pos int, price>=0 ValueError); bulk CHANGED: >=200 x0.88, >=50 x0.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])