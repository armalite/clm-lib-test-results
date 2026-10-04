from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def discount_rate(customer, subtotal, lines):
    return TIER.get(customer.get('tier'), Decimal('0'))
def tax_rate(customer):
    return Decimal('0')
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        sub+=r(q*p)
    d=r(sub*discount_rate(customer,sub,lines))
    t=r((sub-d)*tax_rate(customer))
    return {'subtotal':str(r(sub)),'discount':str(d),'tax':str(t),'total':str(r(sub-d+t))}

def format_money(amount, currency):
    raise NotImplementedError
