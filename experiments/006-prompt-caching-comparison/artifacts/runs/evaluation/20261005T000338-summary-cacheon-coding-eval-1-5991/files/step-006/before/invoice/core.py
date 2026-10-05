"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    subtotal=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        amt=Decimal(q)*p
        if q>=200: amt*=Decimal('0.88')
        elif q>=50: amt*=Decimal('0.95')
        subtotal+=r2(amt)
    discount=r2(subtotal*Decimal('0'))
    tax=r2((subtotal-discount)*Decimal('0.10'))
    total=subtotal-discount+tax
    return {k:str(r2(v)) for k,v in dict(subtotal=subtotal,discount=discount,tax=tax,total=total).items()}

def format_money(amount, currency):
    raise NotImplementedError
