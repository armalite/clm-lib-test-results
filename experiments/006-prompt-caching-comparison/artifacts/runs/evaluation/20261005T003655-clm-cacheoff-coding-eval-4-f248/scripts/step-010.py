import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.index('def compute_invoice');j=s.index('PFX=')
new='''from decimal import ROUND_HALF_EVEN

def _b(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0:
            raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0:
            raise ValueError('price')
    sub=Decimal('0')
    for l in lines:
        if l['qty']==0:
            continue
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200:
            a*=Decimal('0.88')
        elif l['qty']>=50:
            a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal('0'))
    tax=(sub-disc)*Decimal('0.10')
    if customer.get('tax_exempt') is True:
        tax=Decimal('0')
    rs,rd,rt=_b(sub),_b(disc),_b(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}


'''
open(p,'w').write(s[:i]+new+s[j:])
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages released. Stage 4 applied in core.py (banker rounding of exact sub/disc/tax, qty 0 skipped, tax_exempt). Check test result then final.'}]},open('/task/workspace/context.json','w'))