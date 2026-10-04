from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.08'),'silver':Decimal('0.02'),'platinum':Decimal('0.10')}
TAX={'NZ':Decimal('0.15'),'US':Decimal('0')}

def validate(lines):
    if not lines: raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
    lines=[l for l in lines if l['qty']>0]
    if not lines: raise ValueError('all ignored')
    return lines

def compute_invoice(lines, customer):
    lines=validate(lines)
    amounts=[r(Decimal(l['qty'])*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=50 else 1)) for l in lines]
    subtotal=sum(amounts,Decimal(0))
    discount=r(TIER.get(customer.get('tier'),Decimal(0))*sum((a for a,l in zip(amounts,lines) if l['qty']<50),Decimal(0)))
    shipping=Decimal('7.50') if subtotal-discount<Decimal(100) else Decimal(0)
    tax=r((subtotal-discount)*TAX.get(customer.get('region'),Decimal('0.10')))
    total=subtotal-discount+shipping+tax
    return {k:str(r(v)) for k,v in dict(subtotal=subtotal,discount=discount,shipping=shipping,tax=tax,total=total).items()}
