import subprocess,sys,re
p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.index('def compute_invoice');j=s.index('CUR=')
new='''from decimal import ROUND_HALF_EVEN
def rb(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        if q==0: continue
        a=Decimal(q)*p
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal(0))
    tax=Decimal(0) if customer.get('tax_exempt') is True else (sub-disc)*TAX
    s2,d2,t2=rb(sub),rb(disc),rb(tax)
    return {'subtotal':str(s2),'discount':str(d2),'tax':str(t2),'total':str(s2-d2+t2)}

'''
s=s[:i]+new+s[j:]
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done: half-even final rounding, tax_exempt, qty0 skip\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])