from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(subtotal, customer):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

def line_amount(l):
    a=Decimal(int(l['qty']))*Decimal(str(l['unit_price']))
    if int(l['qty'])>=100: a*=Decimal('0.90')
    return r2(a)

def compute_invoice(lines, customer):
    sub=sum((line_amount(l) for l in lines), Decimal('0'))
    disc=r2(sub*discount_rate(sub,customer))
    tax=r2((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

def format_money(amount, currency):
    raise NotImplementedError
