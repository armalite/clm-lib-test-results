p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.index('def compute_invoice')
s=s[:i]+'''def _calc(lines, customer, ship=True):
    _validate(lines)
    lines=[l for l in lines if l['qty']>0]
    if not lines:
        raise ValueError('all ignored')
    amts=[l['qty']*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=BULK else 1) for l in lines]
    subtotal=sum(amts,Decimal('0'))
    elig=sum((a for a,l in zip(amts,lines) if l['qty']<BULK),Decimal('0'))
    discount=TIER.get(customer.get('tier'),Decimal('0'))*elig
    c=customer.get('coupon')
    c=Decimal(str(c)) if c not in (None,'') else Decimal('0')
    discount=discount+max(Decimal('0'),min(c,subtotal-discount))
    net=subtotal-discount
    shipping=(Decimal('7.50') if net<Decimal('100.00') else Decimal('0')) if ship else Decimal('0')
    tax=(net+shipping)*TAX.get(customer.get('region'),Decimal('0.10'))
    st,d,t=rb(subtotal),rb(discount),rb(tax)
    sh=shipping.quantize(Q)
    return {'subtotal':st,'discount':d,'shipping':sh,'tax':t,'total':st-d+sh+t}

def rb(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    return {k:str(v) for k,v in _calc(lines,customer).items()}

def compute_refund(lines, customer, returns):
    _validate(lines)
    skus={}
    for l in lines:
        skus[l.get('sku')]=skus.get(l.get('sku'),0)+l['qty']
    for k,v in (returns or {}).items():
        if k not in skus or isinstance(v,bool) or not isinstance(v,int) or v<1 or v>skus[k]:
            raise ValueError('bad return')
    orig=_calc(lines,customer,False)['total']
    rem=dict(returns or {})
    kept=[]
    for l in lines:
        q=l['qty']; take=min(q,rem.get(l.get('sku'),0))
        if l.get('sku') in rem: rem[l.get('sku')]-=take
        if q-take>0:
            n=dict(l); n['qty']=q-take; kept.append(n)
    kt=_calc(kept,customer,False)['total'] if kept else Decimal('0')
    return str(max(Decimal('0'),orig-kt).quantize(Q))
'''
s=s.replace('ROUND_HALF_UP,','ROUND_HALF_UP, ROUND_HALF_EVEN,')
open(p,'w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, compute_refund\n__all__=["compute_invoice","compute_refund"]\n')
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(q.stderr[-2000:])