code='''from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
def bulk(q):
    if q>=200: return Decimal('0.88')
    if q>=50: return Decimal('0.95')
    return Decimal('1')
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('negative price')
        sub+=Decimal(q)*p*bulk(q)
    rate=TIER.get(customer.get('tier'),Decimal('0'))
    disc=sub*rate
    tax=(sub-disc)*Decimal('0.10')
    s,d,t=r2(sub),r2(disc),r2(tax)
    tot=s-d+t
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(r2(tot))}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('S3: tier disc gold5 silver2; rounding CHANGED: exact, then half-even on sub/disc/tax.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])