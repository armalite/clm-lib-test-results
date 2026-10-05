from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def be2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def discount_rate(lines, customer, subtotal):
    return TIER.get((customer or {}).get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def line_amount(l):
    q=Decimal(str(l['qty']))
    a=q*Decimal(str(l['unit_price']))
    if q>=100:
        a=a*Decimal('0.90')
    return a

def compute_invoice(lines, customer):
    customer=customer or {}
    sub=sum((line_amount(l) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines,customer,sub)
    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)
    s,d,t=be2(sub),be2(disc),be2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(s-d+t)}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+'{:,.2f}'.format(abs(a))
