from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def _r(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def tax_rate(customer):
    if customer.get('tax_exempt') is True: return Decimal('0')
    return Decimal('0.10')

def discount_rate(customer, subtotal):
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal('0'))

def _he(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price']))*(Decimal('0.90') if Decimal(str(l['qty']))>=100 else 1) for l in lines), Decimal('0'))
    disc=sub*discount_rate(customer, sub)
    tax=(sub-disc)*tax_rate(customer)
    rs,rd,rt=_he(sub),_he(disc),_he(tax)
    tot=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(tot)}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=_r(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+'{:,.2f}'.format(abs(a))
