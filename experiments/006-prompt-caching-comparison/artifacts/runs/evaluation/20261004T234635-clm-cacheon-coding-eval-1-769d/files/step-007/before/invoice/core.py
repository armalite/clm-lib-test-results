from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('bad qty')
        up=Decimal(str(l['unit_price']))
        if up<0: raise ValueError('negative price')
        a=Decimal(q)*up
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
        sub+=r2(a)
    disc=r2(sub*Decimal(0))
    tax=r2((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}

def format_money(amount, currency):
    raise NotImplementedError
