from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(lines, customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return Decimal('0.10')

def validate(lines, customer):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0:
            raise ValueError('qty')
        try:
            p=Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('price')
        if not p.is_finite() or p<0:
            raise ValueError('price')

def line_amount(l):
    a=l['qty']*Decimal(str(l['unit_price']))
    if l['qty']>=100:
        a=a*Decimal('0.90')
    return a

def compute_invoice(lines, customer):
    validate(lines, customer)
    sub=sum((_r(line_amount(l)) for l in lines if l['qty']!=0), Decimal('0'))
    disc=_r(sub*discount_rate(lines,customer,sub))
    tax=_r((sub-disc)*tax_rate(lines,customer))
    tot=sub-disc+tax
    return {k:str(_r(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('currency')
    a=_r(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+'{:,.2f}'.format(_r(abs(Decimal(str(a)))))
