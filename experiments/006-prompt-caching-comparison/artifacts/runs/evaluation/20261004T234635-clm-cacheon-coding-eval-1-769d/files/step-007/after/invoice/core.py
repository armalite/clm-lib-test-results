from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)

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
        sub+=a
    rate={'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get((customer or {}).get('tier'),Decimal(0))
    d=sub*rate
    t=(sub-d)*Decimal('0.10')
    sub,disc,tax=r2(sub),r2(d),r2(t)
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}

def format_money(amount, currency):
    raise NotImplementedError
