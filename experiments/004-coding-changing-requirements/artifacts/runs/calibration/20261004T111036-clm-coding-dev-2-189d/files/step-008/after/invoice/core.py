from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def discount_rate(customer):
    return TIER.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    if customer.get('tax_exempt') is True: return Decimal('0')
    return Decimal('0.10')

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')
    sub=sum((r2(int(l['qty'])*Decimal(str(l['unit_price']))) for l in lines),Decimal('0'))
    sub=r2(sub)
    disc=r2(sub*discount_rate(customer))
    tax=r2((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX: raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PFX[currency]+'{:,.2f}'.format(abs(a))
