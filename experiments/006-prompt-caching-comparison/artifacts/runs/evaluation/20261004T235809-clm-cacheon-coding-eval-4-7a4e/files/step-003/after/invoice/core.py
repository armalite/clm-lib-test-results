from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def line_amount(l, customer):
    a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
    if l['qty']>=100:
        a*=Decimal('0.90')
    return r2(a)

def discount_rate(customer, subtotal, lines):
    return TIER.get(customer.get('tier'),Decimal(0))

def tax_rate(customer, lines):
    return Decimal(0)

def compute_invoice(lines, customer):
    sub=sum((line_amount(l,customer) for l in lines),Decimal(0))
    disc=r2(sub*discount_rate(customer,sub,lines))
    tax=r2((sub-disc)*tax_rate(customer,lines))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}

def format_money(amount, currency):
    raise NotImplementedError
