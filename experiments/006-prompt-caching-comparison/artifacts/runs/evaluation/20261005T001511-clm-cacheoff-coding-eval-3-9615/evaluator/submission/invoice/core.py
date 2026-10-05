from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(lines, customer, subtotal):
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get((customer or {}).get('tier'),Decimal('0'))

def _b(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def tax_rate(customer):
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get((customer or {}).get('region'),Decimal('0.12'))

def _amt(l):
    q=int(l['qty'])
    a=q*Decimal(str(l['unit_price']))
    if q>=200:
        a=a*Decimal('0.88')
    elif q>=50:
        a=a*Decimal('0.95')
    return a

def compute_invoice(lines, customer):
    customer=customer or {}
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('qty')
        if Decimal(str(l['unit_price']))<0:
            raise ValueError('price')
    sub=sum((_amt(l) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines, customer, sub)
    tax=(sub-disc)*tax_rate(customer)
    if customer.get('tax_exempt') is True:
        tax=Decimal('0')
    rs,rd,rt=_b(sub),_b(disc),_b(tax)
    total=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(total)}

_P={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in _P:
        raise ValueError(currency)
    a=_r(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+_P[currency]+'{:,.2f}'.format(abs(a))
