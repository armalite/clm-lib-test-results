from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0:
            raise ValueError('bad qty')
        p=Decimal(str(l.get('unit_price')))
        if p<0:
            raise ValueError('negative price')
        sub+=_r(q*p)
    disc=_r(sub*Decimal(0))
    tax=_r((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {'subtotal':str(_r(sub)),'discount':str(disc),'tax':str(tax),'total':str(_r(tot))}

def format_money(amount, currency):
    raise NotImplementedError
