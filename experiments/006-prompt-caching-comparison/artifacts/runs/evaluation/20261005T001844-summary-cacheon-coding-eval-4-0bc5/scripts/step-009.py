s=open('/task/workspace/invoice/core.py').read()
i=s.index('def compute_invoice');j=s.index('PFX=')
new='''from decimal import ROUND_HALF_EVEN
def r2e(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0)
    for l in lines:
        q=l['qty']
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        if q==0: continue
        a=Decimal(q)*p
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal(0))
    tax=Decimal(0) if customer.get('tax_exempt') is True else (sub-disc)*TAX
    rs,rd,rt=r2e(sub),r2e(disc),r2e(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(r2e(rs-rd+rt))}

'''
s=s[:i]+new+s[j:]
open('/task/workspace/invoice/core.py','w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done: exact calc, half-even, qty0 skip, tax_exempt\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])