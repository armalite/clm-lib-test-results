from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

from decimal import ROUND_HALF_EVEN

def _b(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0:
            raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0:
            raise ValueError('price')
    sub=Decimal('0')
    for l in lines:
        if l['qty']==0:
            continue
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200:
            a*=Decimal('0.88')
        elif l['qty']>=50:
            a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal('0'))
    tax=(sub-disc)*Decimal('0.10')
    if customer.get('tax_exempt') is True:
        tax=Decimal('0')
    rs,rd,rt=_b(sub),_b(disc),_b(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}


PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('currency')
    d=_r(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+PFX[currency]+str(abs(d))
