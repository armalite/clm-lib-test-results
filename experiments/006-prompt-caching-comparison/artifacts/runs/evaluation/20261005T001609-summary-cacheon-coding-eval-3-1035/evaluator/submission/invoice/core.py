from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
Q=Decimal('0.01')
def r2(x,m=ROUND_HALF_UP):return Decimal(x).quantize(Q,rounding=m)
def re(x):return r2(x,ROUND_HALF_EVEN)
TAX_RATE=Decimal('0.10')
TIERS={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def discount_rate(lines,customer,subtotal):return TIERS.get(customer.get('tier'),Decimal(0))
def tax_rate(customer):
    if customer.get('tax_exempt') is True:return Decimal(0)
    return REG.get(customer.get('region'),Decimal('0.12'))
REG={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}
def line_amt(l):
    a=int(l['qty'])*Decimal(str(l['unit_price']))
    q=int(l['qty'])
    if q>=200:a=a*Decimal('0.88')
    elif q>=50:a=a*Decimal('0.95')
    return a
def compute_invoice(lines,customer):
    if not lines:raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:raise ValueError('qty')
        if Decimal(str(l['unit_price']))<0:raise ValueError('price')
    sub=sum((line_amt(l) for l in lines),Decimal(0))
    disc=sub*discount_rate(lines,customer,sub)
    tax=(sub-disc)*tax_rate(customer)
    rs,rd,rt=re(sub),re(disc),re(tax)
    tot=rs-rd+rt
    return {k:str(r2(v)) for k,v in (('subtotal',rs),('discount',rd),('tax',rt),('total',tot))}
PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount,currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+'{:,}'.format(abs(a))
