from decimal import Decimal, ROUND_HALF_EVEN

Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

TIERS={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def discount_rate(lines, customer, subtotal):
    return TIERS.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    if customer.get('tax_exempt') is True: return Decimal('0')
    return Decimal('0.10')

def compute_invoice(lines, customer):
    sub=sum((Decimal(l['qty'])*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines, customer, sub)
    tax=(sub-disc)*tax_rate(customer)
    s,d,t=r2(sub),r2(disc),r2(tax)
    total=s-d+t
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(r2(total))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=Decimal(str(amount)).quantize(Q)
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
