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
            p=Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('bad price')
        if not p.is_finite() or p<0:
            raise ValueError('negative price')

def discount_rate(lines, customer, subtotal):
    return {'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))

from decimal import ROUND_HALF_EVEN
def _re(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def _line(l):
    a=l['qty']*Decimal(str(l['unit_price']))
    if l['qty']>=100:
        a=a*Decimal('0.90')
    return a

def compute_invoice(lines, customer):
    _validate(lines)
    sub=sum((_line(l) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines,customer,sub)
    tax=(sub-disc)*tax_rate(customer)
    rs,rd,rt=_re(sub),_re(disc),_re(tax)
    total=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(total)}

def format_money(amount, currency):
    p={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in p:
        raise ValueError(currency)
    d=Decimal(str(amount)).quantize(Decimal('0.01'),rounding=ROUND_HALF_EVEN)
    neg=d<0
    return ('-' if neg else '')+p[currency]+str(abs(d))
