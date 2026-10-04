from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def discount_rate(lines, customer):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return Decimal('0.10')

def validate(lines):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('qty')
        if Decimal(l['unit_price'])<0:
            raise ValueError('price')

def compute_invoice(lines, customer):
    validate(lines)
    subtotal=sum((r2(Decimal(l['qty'])*Decimal(l['unit_price'])) for l in lines), Decimal('0'))
    discount=r2(subtotal*discount_rate(lines, customer))
    tax=r2((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+tax
    return {k:str(r2(v)) for k,v in (('subtotal',subtotal),('discount',discount),('tax',tax),('total',total))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a=r2(Decimal(amount))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+'{:,.2f}'.format(abs(a))
