from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0)
    for l in lines:
        q=l['qty']
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        a=Decimal(q)*p
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
        sub+=r(a)
    disc=r(sub*Decimal(0))
    tax=r((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {'subtotal':str(r(sub)),'discount':str(disc),'tax':str(tax),'total':str(r(tot))}
