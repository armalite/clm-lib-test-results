"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_UP

C=Decimal('0.01')
def r2(x): return x.quantize(C, rounding=ROUND_HALF_UP)

TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}

def line_amount(l):
    a=Decimal(l['qty'])*Decimal(l['unit_price'])
    if l['qty']>=100: a*=Decimal('0.90')
    return r2(a)

def discount_rate(customer, subtotal):
    return TIER.get(customer.get('tier'),Decimal(0))

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')
    sub=sum((line_amount(l) for l in lines),Decimal(0))
    disc=r2(sub*discount_rate(customer,sub))
    tax=r2((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

def format_money(amount, currency):
    raise NotImplementedError
