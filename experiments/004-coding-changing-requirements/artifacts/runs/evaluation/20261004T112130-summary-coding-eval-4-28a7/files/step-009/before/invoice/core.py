from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}
TAX=Decimal('0.10')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        a=Decimal(q)*p
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
        sub+=r(a)
    disc=r(sub*TIER.get(customer.get('tier'),Decimal(0)))
    tax=r((sub-disc)*TAX)
    tot=sub-disc+tax
    return {'subtotal':str(r(sub)),'discount':str(disc),'tax':str(tax),'total':str(r(tot))}

CUR={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in CUR: raise ValueError('bad currency')
    try: d=Decimal(str(amount))
    except Exception: raise ValueError('bad amount')
    d=r(d)
    sign='-' if d<0 else ''
    return sign+CUR[currency]+str(abs(d))
