from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def _bulk(qty):
    if qty>=200: return Decimal('0.88')
    if qty>=50: return Decimal('0.95')
    return Decimal('1')

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except (InvalidOperation,KeyError): raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        sub+=Decimal(q)*p*_bulk(q)
    rate=TIER.get((customer or {}).get('tier'),Decimal('0'))
    disc=sub*rate
    c=customer or {}
    trate={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(c.get('region'),Decimal('0.12'))
    if c.get('tax_exempt') is True: trate=Decimal('0')
    tax=(sub-disc)*trate
    rs,rd,rt=r2(sub),r2(disc),r2(tax)
    tot=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(r2(tot))}

PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError('bad currency')
    try: a=Decimal(str(amount))
    except InvalidOperation: raise ValueError('bad amount')
    if not a.is_finite(): raise ValueError('bad amount')
    a=r2(a)
    neg=a<0
    body=str(abs(a))
    return ('-' if neg else '')+PFX[currency]+body
