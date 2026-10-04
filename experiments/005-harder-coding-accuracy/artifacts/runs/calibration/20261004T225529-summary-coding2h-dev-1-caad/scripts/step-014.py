code='''from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal('0.01')
TIER={'gold':Decimal('0.08'),'silver':Decimal('0.02'),'platinum':Decimal('0.10')}
RATES={'NZ':Decimal('0.15'),'US':Decimal('0')}
def r(x): return x.quantize(Q,rounding=ROUND_HALF_EVEN)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0); elig=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        p=Decimal(str(l.get('unit_price')))
        if p<0: raise ValueError('price')
        a=q*p
        if q>=100: a=a*Decimal('0.90')
        else: elig+=a
        sub+=a
    disc=TIER.get(customer.get('tier'),Decimal(0))*elig
    ship=Decimal('7.50') if sub-disc<Decimal('100') else Decimal('0.00')
    tax=(sub-disc+ship)*RATES.get(customer.get('region'),Decimal('0.10'))
    rs,rd,rt=r(sub),r(disc),r(tax)
    tot=rs-rd+ship+rt
    return {'subtotal':str(rs),'discount':str(rd),'shipping':str(r(ship)),'tax':str(rt),'total':str(r(tot))}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('stage6: exact math, final half-even round; shipping taxed\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])