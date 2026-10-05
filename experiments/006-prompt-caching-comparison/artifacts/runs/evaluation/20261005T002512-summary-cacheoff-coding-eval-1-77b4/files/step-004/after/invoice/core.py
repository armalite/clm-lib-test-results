from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def _bulk(qty):
    if qty>=200: return Decimal('0.88')
    if qty>=50: return Decimal('0.95')
    return Decimal('1')

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except (InvalidOperation,KeyError): raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        a=Decimal(q)*p*_bulk(q)
        sub+=r2(a)
    disc=r2(sub*Decimal('0'))
    tax=r2((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

def format_money(amount, currency):
    raise NotImplementedError
