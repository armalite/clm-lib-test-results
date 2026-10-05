from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<0:
            raise ValueError('qty')
        if q==0:
            continue
        p=Decimal(str(l['unit_price']))
        if p<0:
            raise ValueError('price')
        amt=q*p
        if q>=100:
            amt=amt*Decimal('0.90')
        sub+=_r(amt)
    disc=_r(sub*TIER.get(customer.get('tier'),Decimal('0')))
    rate=Decimal('0.10')
    tax=_r((sub-disc)*rate)
    tot=sub-disc+tax
    return {'subtotal':str(_r(sub)),'discount':str(disc),'tax':str(tax),'total':str(_r(tot))}

PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('currency')
    a=_r(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PFX[currency]+str(abs(a))
