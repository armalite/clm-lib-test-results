from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

Q=Decimal('0.01')
def r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        try:
            p=Decimal(str(l.get('unit_price')))
        except (InvalidOperation,TypeError):
            raise ValueError('bad price')
        if not p.is_finite() or p<0:
            raise ValueError('bad price')

def compute_invoice(lines, customer):
    _validate(lines)
    amts=[r(l['qty']*Decimal(str(l['unit_price']))) for l in lines]
    subtotal=sum(amts,Decimal('0'))
    discount=r(TIER.get(customer.get('tier'),Decimal('0'))*subtotal)
    net=subtotal-discount
    shipping=Decimal('7.50') if net<Decimal('100.00') else Decimal('0')
    tax=Decimal('0')
    total=net+shipping+tax
    return {k:str(r(v)) for k,v in [('subtotal',subtotal),('discount',discount),('shipping',shipping),('tax',tax),('total',total)]}
