from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')
        if Decimal(str(l['unit_price']))<0: raise ValueError('price')
    sub=Decimal('0')
    for l in lines:
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=100: a*=Decimal('0.90')
        sub+=r2(a)
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal('0')))
    tax=r2((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {'subtotal':str(r2(sub)),'discount':str(disc),'tax':str(tax),'total':str(r2(tot))}

def format_money(amount, currency):
    raise NotImplementedError
