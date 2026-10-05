code='''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
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
        sub+=r2(a)
    disc=r2(sub*Decimal(0))
    tax=r2((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}
def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
note='Rules so far: API compute_invoice(lines,customer)->dict of 2dp strs subtotal/discount/tax/total; format_money stub. S1: round line half-up before sum, discount=r2(sub*rate) (rate 0), tax=r2((sub-disc)*0.10), total=sub-disc+tax. S2: ValueError on empty lines/qty not positive int/neg price; bulk qty>=200 x0.88, >=50 x0.95. Implemented in invoice/core.py (stage2 done).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))