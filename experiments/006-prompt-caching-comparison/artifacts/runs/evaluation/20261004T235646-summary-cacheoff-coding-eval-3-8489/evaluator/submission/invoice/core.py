from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
Q=Decimal('0.01')
def _r(x, m=ROUND_HALF_EVEN): return x.quantize(Q, rounding=m)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def _discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def _tax_rate(customer):
    if customer.get('tax_exempt') is True: return Decimal('0')
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))

def _line(l):
    q=int(l['qty']); a=q*Decimal(str(l['unit_price']))
    if q>=200: a=a*Decimal('0.88')
    elif q>=50: a=a*Decimal('0.95')
    return a

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        if Decimal(str(l['unit_price']))<0: raise ValueError('price')
    sub=sum((_line(l) for l in lines), Decimal('0'))
    disc=sub*_discount_rate(lines, customer, sub)
    tax=(sub-disc)*_tax_rate(customer)
    s,d,t=_r(sub),_r(disc),_r(tax)
    total=s-d+t
    return {k:str(_r(v)) for k,v in dict(subtotal=s,discount=d,tax=t,total=total).items()}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=_r(Decimal(str(amount)), ROUND_HALF_UP)
    s='-' if a<0 else ''
    return f"{s}{PREFIX[currency]}{abs(a):,.2f}"
