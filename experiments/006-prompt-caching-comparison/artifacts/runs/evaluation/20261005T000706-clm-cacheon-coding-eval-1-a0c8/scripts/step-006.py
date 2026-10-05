code='''from decimal import Decimal, ROUND_HALF_EVEN
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
    rate=RATES.get(tier,Decimal(0))
    disc=sub*rate
    tax=(sub-disc)*Decimal('0.10')
    s,d,t=r2(sub),r2(disc),r2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(r2(s-d+t))}
def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
note='Rules: compute_invoice(lines,customer)->dict 2dp strs subtotal/discount/tax/total; format_money stub. ValueError empty/qty not pos int/neg price; bulk qty>=200 x0.88,>=50 x0.95. S3: tier gold 5% silver 2% else 0; no line rounding, exact sub/disc/tax then half-even round each, total=sum of rounded. In invoice/core.py (stage3 done).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))