from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

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

TIERS={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def _tier_rate(customer):
    t=(customer or {}).get('tier') if isinstance(customer,dict) else None
    return TIERS.get(t,Decimal('0'))

REG={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}

def _tax_rate(customer):
    c=customer if isinstance(customer,dict) else {}
    if c.get('tax_exempt') is True:
        return Decimal('0')
    return REG.get(c.get('region'),Decimal('0.12'))

def compute_invoice(lines, customer):
    _validate(lines)
    sub=Decimal('0')
    for l in lines:
        q=l['qty']
        sub+=Decimal(q)*Decimal(str(l['unit_price']))*_bulk(q)
    disc=sub*_tier_rate(customer)
    tax=(sub-disc)*_tax_rate(customer)
    rs,rd,rt=_r(sub),_r(disc),_r(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}

PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('bad currency')
    a=Decimal(str(amount)).quantize(Q, rounding=ROUND_HALF_EVEN)
    neg=a<0
    return ('-' if neg else '')+PFX[currency]+str(abs(a))
