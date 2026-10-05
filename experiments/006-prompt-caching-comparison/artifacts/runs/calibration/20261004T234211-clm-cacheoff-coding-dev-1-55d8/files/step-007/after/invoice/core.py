from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def _e(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0:
            raise ValueError('bad qty')
        p=Decimal(str(l.get('unit_price')))
        if p<0:
            raise ValueError('negative price')
        a=q*p
        if q>=100:
            a=a*Decimal('0.90')
        sub+=a
    disc=(sub*{'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal(0)))
    tax=((sub-disc)*{'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}.get(customer.get('region'),Decimal('0.12')))
    rs,rd,rt=_e(sub),_e(disc),_e(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}

def format_money(amount, currency):
    raise NotImplementedError
