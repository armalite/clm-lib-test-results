"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def discount_rate(customer, subtotal):
    return TIER.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    return Decimal('0')

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0:
            raise ValueError('bad qty')
        p=Decimal(str(l.get('unit_price')))
        if p<0:
            raise ValueError('negative price')
        sub+=r2(q*p)
    disc=r2(sub*discount_rate(customer,sub))
    tax=r2((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

def format_money(amount, currency):
    raise NotImplementedError
