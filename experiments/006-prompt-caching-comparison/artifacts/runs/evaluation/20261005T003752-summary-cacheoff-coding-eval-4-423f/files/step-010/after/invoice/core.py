"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def discount_rate(customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def line_amount(line):
    amt=Decimal(line['qty'])*Decimal(str(line['unit_price']))
    if line['qty']>=200:
        amt*=Decimal('0.88')
    elif line['qty']>=50:
        amt*=Decimal('0.95')
    return amt

def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0:
            raise ValueError('bad qty')
        try:
            pr=Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if not pr.is_finite() or pr<0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
    sub=sum((line_amount(l) for l in lines if l['qty']!=0), Decimal('0'))
    disc=sub*discount_rate(customer, sub)
    tx=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)
    he=lambda x:x.quantize(Q, rounding=ROUND_HALF_EVEN)
    subtotal,discount,tax=he(sub),he(disc),he(tx)
    total=subtotal-discount+tax
    return {k:str(he(v)) for k,v in (('subtotal',subtotal),('discount',discount),('tax',tax),('total',total))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
