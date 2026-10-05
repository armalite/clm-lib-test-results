from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price')))<0:
            raise ValueError('negative price')

def discount_rate(lines, customer, subtotal):
    return {'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))

def compute_invoice(lines, customer):
    _validate(lines)
    def amt(l):
        a=l['qty']*Decimal(str(l['unit_price']))
        if l['qty']>=100: a=a*Decimal('0.90')
        return a
    sub=sum((amt(l) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines,customer,sub)
    tax=(sub-disc)*tax_rate(customer)
    E=ROUND_HALF_EVEN
    rs,rd,rt=(x.quantize(Q,rounding=E) for x in (sub,disc,tax))
    total=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(total.quantize(Q))}

def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre: raise ValueError('unsupported currency')
    d=Decimal(str(amount)).quantize(Q,rounding=ROUND_HALF_EVEN)
    sign='-' if d<0 else ''
    return sign+pre[currency]+str(abs(d))
