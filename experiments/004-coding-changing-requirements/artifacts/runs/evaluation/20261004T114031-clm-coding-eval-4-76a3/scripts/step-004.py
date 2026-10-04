code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}
TAX=Decimal('0.10')

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        p=Decimal(str(l['unit_price']))
        if p<0:
            raise ValueError('negative price')
        a=Decimal(q)*p
        if q>=100:
            a*=Decimal('0.90')
        sub+=r2(a)
    sub=r2(sub)
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal('0')))
    tax=r2((sub-disc)*TAX)
    total=sub-disc+tax
    return {'subtotal':str(sub),'discount':str(disc),'tax':str(tax),'total':str(r2(total))}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 implemented in invoice/core.py (r2 half-up per line, bulk qty>=100 x0.90, TIER dict platinum10/gold7/silver3, TAX=0.10, validation ValueError). format_money stub exists (NotImplementedError) - likely later stage. Next: advance to stage 3.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))