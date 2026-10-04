from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}
def discount_rate(customer, subtotal, lines):
    return TIER.get(customer.get('tier'), Decimal('0'))
def tax_rate(customer):
    return Decimal('0.10')
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        if q==0: continue
        amt=q*p
        if q>=100: amt=amt*Decimal('0.90')
        sub+=r(amt)
    d=r(sub*discount_rate(customer,sub,lines))
    t=r((sub-d)*tax_rate(customer))
    if customer.get('tax_exempt') is True: t=Decimal('0.00')
    return {'subtotal':str(r(sub)),'discount':str(d),'tax':str(t),'total':str(r(sub-d+t))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError('currency')
    a=r(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+'{:,.2f}'.format(abs(a))
