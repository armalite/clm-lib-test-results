from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        try:
            p=Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if not p.is_finite() or p<0:
            raise ValueError('negative price')

def _bulk(q):
    if q>=200: return Decimal('0.88')
    if q>=50: return Decimal('0.95')
    return Decimal('1')

def compute_invoice(lines, customer):
    _validate(lines)
    sub=Decimal('0')
    for l in lines:
        q=l['qty']
        a=Decimal(q)*Decimal(str(l['unit_price']))*_bulk(q)
        sub+=_r(a)
    disc=_r(sub*Decimal('0'))
    tax=_r((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {'subtotal':str(_r(sub)),'discount':str(disc),'tax':str(tax),'total':str(_r(tot))}

def format_money(amount, currency):
    raise NotImplementedError
