from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def _validate(lines):
    if not lines: raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')

def compute_invoice(lines, customer):
    _validate(lines)
    amounts=[r2(int(l['qty'])*Decimal(str(l['unit_price']))*(Decimal('0.90') if int(l['qty'])>=100 else 1)) for l in lines]
    subtotal=sum(amounts,Decimal('0'))
    eligible=sum((a for a,l in zip(amounts,lines) if int(l['qty'])<100),Decimal('0'))
    tier_disc=r2(TIER.get(customer.get('tier'),Decimal('0'))*eligible)
    discount=tier_disc
    shipping=Decimal('7.50') if subtotal-discount<Decimal('100.00') else Decimal('0')
    tax=r2((subtotal-discount)*Decimal('0.10'))
    total=subtotal-discount+shipping+tax
    return {k:str(r2(v)) for k,v in [('subtotal',subtotal),('discount',discount),('shipping',shipping),('tax',tax),('total',total)]}
