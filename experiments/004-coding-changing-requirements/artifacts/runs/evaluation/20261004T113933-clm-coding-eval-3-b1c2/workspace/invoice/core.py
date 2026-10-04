from decimal import Decimal, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

def discount_rate(lines, customer, subtotal):
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))

def bulk(q):
    return Decimal('0.88') if q>=200 else (Decimal('0.95') if q>=50 else Decimal('1'))

def validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')

def compute_invoice(lines, customer):
    validate(lines)
    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price']))*bulk(l['qty']) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines, customer, sub)
    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)
    s,d,t=r2(sub),r2(disc),r2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(s-d+t)}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+'{:,.2f}'.format(abs(a))
