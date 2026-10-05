src='''from decimal import Decimal, ROUND_HALF_UP

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
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal('0')))
    tax=r2((sub-disc)*TAX)
    tot=sub-disc+tax
    return {'subtotal':str(r2(sub)),'discount':str(disc),'tax':str(tax),'total':str(r2(tot))}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
n='Stage1: line=qty*price, qty>=100 x0.90, round each line half-up; disc=r2(sub*tier); tax=r2((sub-disc)*rate); total. Stage2: tax 10% all; ValueError on empty lines/qty not pos int/negative price; tiers platinum10 gold7 silver3. Implemented in invoice/core.py (r2, TIER, TAX consts). format_money stub exists (unspecified yet). Stage reqs at /task/fixtures/stage-N/REQUIREMENTS.md.'
json.dump({'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':n}]},open('/task/workspace/context.json','w'))