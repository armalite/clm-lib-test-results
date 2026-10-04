from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def compute_invoice(lines, customer):
    amts=[r2(int(l['qty'])*Decimal(l['unit_price'])) for l in lines]
    sub=sum(amts,Decimal(0))
    disc=r2(TIER.get(customer.get('tier'),Decimal(0))*sub)
    ship=Decimal(0)
    tax=r2((sub-disc)*0)
    tot=sub-disc+ship+tax
    return {k:str(r2(v)) for k,v in dict(subtotal=sub,discount=disc,shipping=ship,tax=tax,total=tot).items()}
