from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
def compute_invoice(lines, customer):
    sub=Decimal('0')
    for l in lines:
        a=Decimal(int(l['qty']))*Decimal(str(l['unit_price']))
        if l['qty']>=100: a*=Decimal('0.90')
        sub+=r2(a)
    sub=r2(sub)
    disc=r2(sub*Decimal('0'))
    tax=r2((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}
