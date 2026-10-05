from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def _e(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        p=Decimal(str(l['unit_price']))
        if p<0:
            raise ValueError('negative price')
        a=q*p
        if q>=100: a*=Decimal('0.90')
        sub+=a
    disc=(sub*{'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}.get(customer.get('tier'),Decimal('0')))
    rate={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))
    tax=(sub-disc)*rate
    rs,rd,rt=_e(sub),_e(disc),_e(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}

def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}.get(currency)
    if pre is None:
        raise ValueError('bad currency')
    d=_r(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+pre+str(abs(d))
