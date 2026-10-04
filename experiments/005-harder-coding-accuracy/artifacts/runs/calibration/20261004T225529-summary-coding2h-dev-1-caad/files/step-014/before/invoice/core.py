from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'gold':Decimal('0.08'),'silver':Decimal('0.02'),'platinum':Decimal('0.10')}

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0); tier_elig=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        a=q*p
        if q>=100: a=a*Decimal('0.90')
        sub+=r(a)
        if q<100: tier_elig+=r(a)
    disc=r(TIER.get(customer.get('tier'),Decimal(0))*tier_elig)
    ship=Decimal('7.50') if sub-disc<Decimal('100.00') else Decimal(0)
    rate={'NZ':Decimal('0.15'),'US':Decimal(0)}.get(customer.get('region'),Decimal('0.10'))
    tax=r((sub-disc)*rate)
    tot=sub-disc+ship+tax
    return {k:str(r(v)) for k,v in [('subtotal',sub),('discount',disc),('shipping',ship),('tax',tax),('total',tot)]}
