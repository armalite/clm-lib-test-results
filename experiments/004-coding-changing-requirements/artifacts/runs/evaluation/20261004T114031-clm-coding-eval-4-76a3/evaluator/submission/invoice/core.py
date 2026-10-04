from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}
TAX=Decimal('0.10')

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0:
            raise ValueError('bad qty')
        p=Decimal(str(l['unit_price']))
        if p<0:
            raise ValueError('negative price')
        if q==0:
            continue
        a=Decimal(q)*p
        if q>=200:
            a*=Decimal('0.88')
        elif q>=50:
            a*=Decimal('0.95')
        sub+=a
    from decimal import ROUND_HALF_EVEN
    be=lambda x:x.quantize(Q,rounding=ROUND_HALF_EVEN)
    d=sub*TIER.get(customer.get('tier'),Decimal('0'))
    t=Decimal('0') if customer.get('tax_exempt') is True else (sub-d)*TAX
    sub,disc,tax=be(sub),be(d),be(t)
    total=sub-disc+tax
    return {'subtotal':str(sub),'discount':str(disc),'tax':str(tax),'total':str(r2(total))}


PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    d=r2(Decimal(str(amount)))
    neg=d<0
    return ('-' if neg else '')+PREFIX[currency]+'{:.2f}'.format(abs(d))
