from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        if q==0: continue
        amt=q*p
        if q>=100: amt=amt*Decimal('0.90')
        sub+=r2(amt)
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal(0)))
    rate=Decimal('0.10')
    tax=r2((sub-disc)*rate)
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}

PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError('currency')
    a=r2(Decimal(str(amount)))
    neg=a<0
    return ('-' if neg else '')+PFX[currency]+str(abs(a))
