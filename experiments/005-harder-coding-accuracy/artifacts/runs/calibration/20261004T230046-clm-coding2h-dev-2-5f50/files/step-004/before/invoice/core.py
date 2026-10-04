from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    amts=[r(int(l['qty'])*Decimal(l['unit_price'])) for l in lines]
    subtotal=sum(amts,Decimal('0'))
    discount=r(TIER.get(customer.get('tier'),Decimal('0'))*subtotal)
    shipping=Decimal('0')
    tax=Decimal('0')
    total=subtotal-discount+shipping+tax
    return {k:str(r(v)) for k,v in [('subtotal',subtotal),('discount',discount),('shipping',shipping),('tax',tax),('total',total)]}
