"""Invoice core."""
from decimal import Decimal, ROUND_HALF_EVEN

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
TAX={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}
DISC={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

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
        subtotal+=amt
    discount=subtotal*DISC.get((customer or {}).get('tier'),Decimal('0'))
    cust=customer or {}
    rate=TAX.get(cust.get('region'),Decimal('0.12'))
    if cust.get('tax_exempt') is True: rate=Decimal('0')
    tax=(subtotal-discount)*rate
    s,d,t=r2(subtotal),r2(discount),r2(tax)
    total=s-d+t
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(r2(total))}

PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError('bad currency')
    try: a=Decimal(str(amount))
    except Exception: raise ValueError('bad amount')
    if not a.is_finite(): raise ValueError('bad amount')
    a=r2(a)
    neg=a<0
    s=PFX[currency]+str(abs(a))
    return '-'+s if neg else s
