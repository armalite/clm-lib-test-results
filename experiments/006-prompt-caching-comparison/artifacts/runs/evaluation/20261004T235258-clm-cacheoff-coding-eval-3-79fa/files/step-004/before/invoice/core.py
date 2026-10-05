from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def tax_rate(customer):
    return Decimal('0.10')

def discount_rate(customer, subtotal):
    return Decimal('0')

def compute_invoice(lines, customer):
    sub=sum((_r(Decimal(l['qty'])*Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    sub=_r(sub)
    disc=_r(sub*discount_rate(customer, sub))
    tax=_r((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(_r(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=_r(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+str(abs(a))
