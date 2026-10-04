p='/task/workspace/invoice/core.py'
s=open(p).read()
old=s[s.index('    discounts=[tier_rate'):s.index('    shipping=')]
new="    coupon=Decimal(str((customer or {}).get('coupon') or 0))\n    capp=max(Decimal(0),min(coupon,subtotal))\n    discount=capp+tier_rate(customer)*max(elig-capp,Decimal(0))\n"
s=s.replace(old,new)
s=s.replace("def compute_invoice(lines, customer):","def compute_invoice(lines, customer, _noship=False):")
s=s.replace("if subtotal-discount<Decimal('100.00') else Decimal(0)","if subtotal-discount<Decimal('100.00') and not _noship else Decimal(0)")
s+='''
def compute_refund(lines, customer, returns):
    _validate(lines)
    returns=returns or {}
    qty={}
    for l in lines: qty[l['sku']]=qty.get(l['sku'],0)+l['qty']
    for k,v in returns.items():
        if k not in qty: raise ValueError('sku')
        if isinstance(v,bool) or not isinstance(v,int) or v<1 or v>qty[k]: raise ValueError('ret')
    orig=Decimal(compute_invoice(lines,customer,True)['total'])
    rem=dict(returns); kept=[]
    for l in lines:
        r=min(rem.get(l.get('sku'),0),l['qty'])
        if l.get('sku') in rem: rem[l['sku']]-=r
        if l['qty']-r>0:
            d=dict(l); d['qty']=l['qty']-r; kept.append(d)
    kt=Decimal(compute_invoice(kept,customer,True)['total']) if kept else Decimal(0)
    return str(r2(max(orig-kt,Decimal(0))))
'''
open(p,'w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, compute_refund\n__all__=["compute_invoice","compute_refund"]\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])