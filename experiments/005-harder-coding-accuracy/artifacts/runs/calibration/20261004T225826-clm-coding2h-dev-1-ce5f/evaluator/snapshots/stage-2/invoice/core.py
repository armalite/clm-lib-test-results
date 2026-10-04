"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def _validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('price')
        if not p.is_finite() or p<0: raise ValueError('price')

def tier_rate(c): return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get((c or {}).get('tier'),Decimal(0))

def tax_rate(customer): return Decimal('0.10')

def compute_invoice(lines, customer):
    _validate(lines)
    amounts=[r2(l['qty']*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=100 else 1)) for l in lines]
    subtotal=sum(amounts,Decimal(0))
    discounts=[tier_rate(customer)*subtotal]
    discount=sum((r2(d) for d in discounts),Decimal(0))
    shipping=Decimal(0)
    tax=r2((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+shipping+tax
    return {k:str(r2(v)) for k,v in [('subtotal',subtotal),('discount',discount),('shipping',shipping),('tax',tax),('total',total)]}
