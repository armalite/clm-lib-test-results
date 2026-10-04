code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        a=q*p
        if q>=100: a=a*Decimal('0.90')
        sub+=r(a)
    tier_elig=sub
    disc=r(TIER.get(customer.get('tier'),Decimal(0))*tier_elig)
    ship=Decimal(0)
    tax=r((sub-disc)*Decimal('0.10'))
    tot=sub-disc+ship+tax
    return {k:str(r(v)) for k,v in [('subtotal',sub),('discount',disc),('shipping',ship),('tax',tax),('total',tot)]}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('stage2: tier disc gold5 silver2 on subtotal (rounded); bulk qty>=100 x0.90 before line round\n')
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])