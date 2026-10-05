import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
start=s.index('def compute_invoice');end=s.index('PFX=')
new='''def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<0: raise ValueError('qty')
        if Decimal(str(l['unit_price']))<0: raise ValueError('price')
    sub=Decimal('0')
    for l in lines:
        if l['qty']==0: continue
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200: a*=Decimal('0.88')
        elif l['qty']>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal('0'))
    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*Decimal('0.10')
    he=lambda x:x.quantize(Q,rounding=ROUND_HALF_EVEN)
    rs,rd,rt=he(sub),he(disc),he(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}

'''
s=s[:start]+new+s[end:]
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages released. core.py updated for stage 4 (half-even final rounding, no line rounding, tax_exempt, qty 0 skipped) at step 9.'}]},open('/task/workspace/context.json','w'))