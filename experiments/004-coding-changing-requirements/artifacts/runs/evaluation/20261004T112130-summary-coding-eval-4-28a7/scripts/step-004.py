import subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}
TAX=Decimal('0.10')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        a=Decimal(q)*p
        if q>=100: a*=Decimal('0.90')
        sub+=r(a)
    disc=r(sub*TIER.get(customer.get('tier'),Decimal(0)))
    tax=r((sub-disc)*TAX)
    tot=sub-disc+tax
    return {'subtotal':str(r(sub)),'discount':str(disc),'tax':str(tax),'total':str(r(tot))}
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','w').write('stage1+2 done in core.py (tiers plat10 gold7 silver3, tax10%, validation)\n')
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(p.stderr[-1500:])