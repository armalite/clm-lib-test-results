"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price')))<0:
            raise ValueError('negative price')

def discount_rate(customer):
    return TIER.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    _validate(lines)
    sub=sum((_r(l['qty']*Decimal(str(l['unit_price']))) for l in lines),Decimal('0'))
    disc=_r(sub*discount_rate(customer))
    tax=_r((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(_r(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('bad currency')
    a=_r(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PFX[currency]+str(abs(a))
