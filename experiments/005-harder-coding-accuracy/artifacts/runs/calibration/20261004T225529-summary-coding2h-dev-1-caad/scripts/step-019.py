code='''from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal('0.01')
TIER={'gold':Decimal('0.08'),'silver':Decimal('0.02'),'platinum':Decimal('0.10')}
RATES={'NZ':Decimal('0.15'),'US':Decimal('0')}
def r(x): return x.quantize(Q,rounding=ROUND_HALF_EVEN)
def _validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')
def _calc(lines, customer, noship=False):
    _validate(lines)
    sub=Decimal(0); elig=Decimal(0)
    for l in lines:
        q=l['qty']; a=q*Decimal(str(l['unit_price']))
        if q>=50: a=a*Decimal('0.90')
        else: elig+=a
        sub+=a
    c=Decimal(str(customer.get('coupon') or '0'))
    ca=max(Decimal(0),min(c,sub))
    td=TIER.get(customer.get('tier'),Decimal(0))*max(elig-ca,Decimal(0))
    disc=ca+td
    ship=Decimal('0.00') if noship else (Decimal('7.50') if sub-disc<Decimal('100') else Decimal('0.00'))
    tax=(sub-disc+ship)*RATES.get(customer.get('region'),Decimal('0.10'))
    rs,rd,rt=r(sub),r(disc),r(tax)
    return {'subtotal':str(rs),'discount':str(rd),'shipping':str(r(ship)),'tax':str(rt),'total':str(r(rs-rd+ship+rt))}
def compute_invoice(lines, customer):
    return _calc(lines, customer)
def compute_refund(lines, customer, returns):
    orig=Decimal(_calc(lines, customer, True)['total'])
    qty={l.get('sku'):l.get('qty') for l in lines}
    for s,n in (returns or {}).items():
        if s not in qty: raise ValueError('sku')
        if isinstance(n,bool) or not isinstance(n,int) or n<1 or n>qty[s]: raise ValueError('ret')
    kept=[]
    for l in lines:
        k=l['qty']-(returns or {}).get(l['sku'],0)
        if k>0: kept.append(dict(l,qty=k))
    kt=Decimal(_calc(kept, customer, True)['total']) if kept else Decimal('0')
    return str(r(max(orig-kt,Decimal(0))))
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, compute_refund\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])