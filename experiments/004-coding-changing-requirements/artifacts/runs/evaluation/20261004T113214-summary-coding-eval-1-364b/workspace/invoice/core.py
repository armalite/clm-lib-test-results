from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
RATES={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
TAX={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}
PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError('currency')
    d=r(Decimal(str(amount)))
    neg=d<0
    return ('-' if neg else '')+PFX[currency]+str(abs(d))
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
    dr=RATES.get(customer.get('tier'),Decimal(0))
    disc=sub*dr
    tr=TAX.get(customer.get('region'),Decimal('0.12'))
    if customer.get('tax_exempt') is True: tr=Decimal(0)
    tax=(sub-disc)*tr
    rs,rd,rt=r(sub),r(disc),r(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}
