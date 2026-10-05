from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
RATES={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
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
        sub+=a
    tier=(customer or {}).get('tier') if isinstance(customer,dict) else None
    disc=sub*RATES.get(tier,Decimal(0))
    c=customer if isinstance(customer,dict) else {}
    rate={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}.get(c.get('region'),Decimal('0.12'))
    if c.get('tax_exempt') is True: rate=Decimal(0)
    tax=(sub-disc)*rate
    s,d,t=r2(sub),r2(disc),r2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(s-d+t)}
def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre: raise ValueError('currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+pre[currency]+str(abs(a))
