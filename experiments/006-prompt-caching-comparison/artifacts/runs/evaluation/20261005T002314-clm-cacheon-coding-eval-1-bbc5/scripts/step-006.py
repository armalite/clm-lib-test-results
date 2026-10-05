import json,subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
RATES={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0)
    for l in lines:
        q=l['qty']
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        a=Decimal(q)*p
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
        sub+=a
    tier=(customer or {}).get('tier') if isinstance(customer,dict) else None
    disc=sub*RATES.get(tier,Decimal(0))
    tax=(sub-disc)*Decimal('0.10')
    s,d,t=r2(sub),r2(disc),r2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(s-d+t)}
def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-3 in invoice/core.py (Decimal): validation ValueError (empty lines, qty not positive int, price<0); line amt=qty*price *0.88 if qty>=200 elif >=50 *0.95 (unrounded); tier discount gold 5% silver 2% else 0 on exact sub; tax 10% of exact (sub-disc); round sub/disc/tax half-even 2dp; total=sum of rounded; returns dict of str; format_money unimplemented.'}]},open('/task/workspace/context.json','w'))