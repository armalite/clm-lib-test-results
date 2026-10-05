p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.index('def compute_invoice');j=s.index('PREFIX=')
new='''from decimal import ROUND_HALF_EVEN
def re2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('bad qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('negative price')
        if q==0: continue
        a=Decimal(q)*p
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal(0))
    tax=(sub-disc)*TAX
    if customer.get('tax_exempt') is True: tax=Decimal(0)
    rs,rd,rt=re2(sub),re2(disc),re2(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(re2(rs-rd+rt))}

'''
s=s[:i]+new+s[j:]
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])