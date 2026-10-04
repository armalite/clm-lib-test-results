from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
def bulk(q):
    if q>=200: return Decimal('0.88')
    if q>=50: return Decimal('0.95')
    return Decimal('1')
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('negative price')
        sub+=Decimal(q)*p*bulk(q)
    rate=TIER.get(customer.get('tier'),Decimal('0'))
    disc=sub*rate
    tr=REGION.get(customer.get('region'),Decimal('0.12'))
    if customer.get('tax_exempt') is True: tr=Decimal('0')
    tax=(sub-disc)*tr
    s,d,t=r2(sub),r2(disc),r2(tax)
    tot=s-d+t
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(r2(tot))}

REGION={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}
PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError('bad currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
