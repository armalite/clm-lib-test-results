"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_EVEN

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def _validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('price')
        if not p.is_finite() or p<0: raise ValueError('price')

def tier_rate(c): return {'gold':Decimal('0.08'),'silver':Decimal('0.02'),'platinum':Decimal('0.10')}.get((c or {}).get('tier'),Decimal(0))

def tax_rate(customer): return {'NZ':Decimal('0.15'),'US':Decimal('0')}.get((customer or {}).get('region'),Decimal('0.10'))

def compute_invoice(lines, customer):
    _validate(lines)
    amounts=[(l['qty']*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=50 else 1)) for l in lines]
    subtotal=sum(amounts,Decimal(0))
    elig=sum((a for a,l in zip(amounts,lines) if l['qty']<50),Decimal(0))
    discounts=[tier_rate(customer)*elig]
    discount=sum(discounts,Decimal(0))
    coupon=Decimal(str((customer or {}).get('coupon') or 0))
    discount=discount+max(Decimal(0),min(coupon,subtotal-discount))
    shipping=Decimal('7.50') if subtotal-discount<Decimal('100.00') else Decimal(0)
    tax=(subtotal-discount+shipping)*tax_rate(customer)
    subtotal,discount,tax=r2(subtotal),r2(discount),r2(tax)
    total=subtotal-discount+shipping+tax
    return {k:str(r2(v)) for k,v in [('subtotal',subtotal),('discount',discount),('shipping',shipping),('tax',tax),('total',total)]}
