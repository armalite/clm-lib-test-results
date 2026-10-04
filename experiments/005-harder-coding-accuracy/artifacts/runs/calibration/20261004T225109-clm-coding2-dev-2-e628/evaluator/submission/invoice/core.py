from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)
BULK=50
TIER={'gold':Decimal('0.08'),'platinum':Decimal('0.10'),'silver':Decimal('0.02')}
def validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('qty')
        if Decimal(str(l['unit_price']))<0: raise ValueError('price')
def compute_invoice(lines, customer):
    validate(lines)
    lines=[l for l in lines if l['qty']>0]
    if not lines: raise ValueError('empty')
    amts=[r2(l['qty']*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=BULK else 1)) for l in lines]
    sub=sum(amts,Decimal(0))
    elig=sum((a for a,l in zip(amts,lines) if l['qty']<BULK),Decimal(0))
    disc=r2(TIER.get(customer.get('tier'),Decimal(0))*elig)
    ship=Decimal('7.50') if sub-disc<Decimal('100') else Decimal(0)
    rate={'NZ':Decimal('0.15'),'US':Decimal(0)}.get(customer.get('region'),Decimal('0.10'))
    tax=r2((sub-disc)*rate)
    tot=sub-disc+ship+tax
    return {k:str(r2(v)) for k,v in dict(subtotal=sub,discount=disc,shipping=ship,tax=tax,total=tot).items()}
