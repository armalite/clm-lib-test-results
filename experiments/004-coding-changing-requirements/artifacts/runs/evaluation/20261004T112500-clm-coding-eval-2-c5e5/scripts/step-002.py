import json,subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        sub+=r2(q*p)
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal(0)))
    rate=Decimal(0)
    tax=r2((sub-disc)*rate)
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done in invoice/core.py: line round half-up, subtotal, tier discount gold5%/silver2%, tax rate 0 (var rate), ValueError on empty/bad qty/neg price. Outputs str 2dp.'}]}
json.dump(c,open('/task/workspace/context.json','w'))