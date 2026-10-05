from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    sub=Decimal('0')
    for l in lines:
        a=Decimal(int(l['qty']))*Decimal(str(l['unit_price']))
        if int(l['qty'])>=100:
            a=a*Decimal('0.90')
        sub+=_r(a)
    disc=_r(sub*Decimal('0'))
    tax=_r((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {'subtotal':str(_r(sub)),'discount':str(disc),'tax':str(tax),'total':str(_r(tot))}

def format_money(amount, currency):
    raise NotImplementedError
