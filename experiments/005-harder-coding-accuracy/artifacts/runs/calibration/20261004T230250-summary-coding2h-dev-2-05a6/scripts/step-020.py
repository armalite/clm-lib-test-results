code='''from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation
Q=Decimal('0.01')
TIER={'gold':Decimal('0.08'),'platinum':Decimal('0.10'),'silver':Decimal('0.02')}
TAX={'NZ':Decimal('0.15'),'US':Decimal('0')}
def r(x): return x.quantize(Q,rounding=ROUND_HALF_EVEN)
def _dec(s):
    try: d=Decimal(str(s))
    except (InvalidOperation,ValueError,TypeError): raise ValueError('bad decimal')
    if not d.is_finite(): raise ValueError('non-finite')
    return d
def validate(lines):
    if not lines: raise ValueError('empty')
    out=[]
    for l in lines:
        q=l['qty']
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('qty')
        p=_dec(l['unit_price'])
        if p<0: raise ValueError('price')
        if q: out.append((l['sku'],q,p))
    if not out: raise ValueError('all ignored')
    return out
def _compute(lines,customer,ship=True):
    ls=validate(lines)
    sub=Decimal(0); elig=Decimal(0)
    for _,q,p in ls:
        a=q*p
        if q>=50: a=a*Decimal('0.90')
        else: elig+=a
        sub+=a
    tier=elig*TIER.get(customer.get('tier'),Decimal(0))
    c=customer.get('coupon')
    c=Decimal(0) if c is None else _dec(c)
    if c<0: raise ValueError('coupon')
    ca=max(Decimal(0),min(c,sub-tier))
    disc=tier+ca
    shipping=(Decimal('7.50') if sub-disc<100 else Decimal('0.00')) if ship else Decimal('0.00')
    tax=(sub-disc+shipping)*TAX.get(customer.get('region'),Decimal('0.10'))
    rs,rd,rt=r(sub),r(disc),r(tax)
    return {'subtotal':str(rs),'discount':str(rd),'shipping':str(shipping.quantize(Q)),'tax':str(rt),'total':str((rs-rd+shipping+rt).quantize(Q))}
def compute_invoice(lines,customer): return _compute(lines,customer)
def compute_refund(lines,customer,returns):
    orig=Decimal(_compute(lines,customer,False)['total'])
    bysku={l['sku']:l for l in lines}
    for s,n in returns.items():
        if s not in bysku: raise ValueError('sku')
        if isinstance(n,bool) or not isinstance(n,int) or n<1 or n>bysku[s]['qty']: raise ValueError('ret qty')
    kept=[]
    for l in lines:
        k=l['qty']-returns.get(l['sku'],0)
        if k>0: kept.append(dict(l,qty=k))
    kt=Decimal(_compute(kept,customer,False)['total']) if kept else Decimal(0)
    return str(max(Decimal(0),orig-kt).quantize(Q))
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, compute_refund\n')
import subprocess,sys
subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace')