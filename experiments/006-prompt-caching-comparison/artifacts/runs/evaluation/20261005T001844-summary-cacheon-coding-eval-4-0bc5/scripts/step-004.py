open('/task/workspace/invoice/core.py','w').write('''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}
TAX=Decimal('0.10')
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0)
    for l in lines:
        q=l['qty']
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        a=Decimal(q)*p
        if q>=100: a*=Decimal('0.90')
        sub+=r2(a)
    sub=r2(sub)
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal(0)))
    tax=r2((sub-disc)*TAX)
    tot=sub-disc+tax
    return {'subtotal':str(sub),'discount':str(disc),'tax':str(tax),'total':str(r2(tot))}
''')
open('/task/workspace/NOTES.md','w').write('stage1: rounding halfup per line, bulk qty>=100 x0.90, tier\nstage2: tax 10%, validation, tiers plat10 gold7 silver3\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])