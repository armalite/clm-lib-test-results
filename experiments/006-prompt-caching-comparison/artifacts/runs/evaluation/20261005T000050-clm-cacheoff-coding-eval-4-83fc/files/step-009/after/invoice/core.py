from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<0: raise ValueError('qty')
        if Decimal(str(l['unit_price']))<0: raise ValueError('price')
    sub=Decimal('0')
    for l in lines:
        if l['qty']==0: continue
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200: a*=Decimal('0.88')
        elif l['qty']>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal('0'))
    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*Decimal('0.10')
    he=lambda x:x.quantize(Q,rounding=ROUND_HALF_EVEN)
    rs,rd,rt=he(sub),he(disc),he(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}

PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX: raise ValueError('currency')
    d=r2(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+PFX[currency]+str(abs(d))
