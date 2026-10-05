from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    sub=Decimal('0')
    for l in lines:
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=100:
            a*=Decimal('0.90')
        sub+=_r(a)
    disc=_r(sub*TIER.get(customer.get('tier'),Decimal('0')))
    tax=_r((sub-disc)*Decimal('0'))
    tot=sub-disc+tax
    return {k:str(_r(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}


def format_money(amount, currency):
    raise NotImplementedError
