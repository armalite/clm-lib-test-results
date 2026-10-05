from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        if Decimal(str(l['unit_price']))<0:
            raise ValueError('negative price')
    subtotal=Decimal('0')
    for l in lines:
        amt=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200:
            amt*=Decimal('0.88')
        elif l['qty']>=50:
            amt*=Decimal('0.95')
        subtotal+=r2(amt)
    subtotal=r2(subtotal)
    discount=r2(subtotal*Decimal('0'))
    tax=r2((subtotal-discount)*Decimal('0.10'))
    total=subtotal-discount+tax
    return {'subtotal':str(subtotal),'discount':str(discount),'tax':str(tax),'total':str(r2(total))}


def format_money(amount, currency):
    raise NotImplementedError
