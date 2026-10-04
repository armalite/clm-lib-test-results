from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}
TAX=Decimal('0.10')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
from decimal import ROUND_HALF_EVEN
def rb(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        if q==0: continue
        a=Decimal(q)*p
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal(0))
    tax=Decimal(0) if customer.get('tax_exempt') is True else (sub-disc)*TAX
    s2,d2,t2=rb(sub),rb(disc),rb(tax)
    return {'subtotal':str(s2),'discount':str(d2),'tax':str(t2),'total':str(s2-d2+t2)}

CUR={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in CUR: raise ValueError('bad currency')
    try: d=Decimal(str(amount))
    except Exception: raise ValueError('bad amount')
    d=r(d)
    sign='-' if d<0 else ''
    return sign+CUR[currency]+str(abs(d))
