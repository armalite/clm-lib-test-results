from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    amounts=[r2(int(l['qty'])*Decimal(str(l['unit_price']))) for l in lines]
    subtotal=sum(amounts,Decimal('0'))
    tier_disc=r2(TIER.get(customer.get('tier'),Decimal('0'))*subtotal)
    discount=tier_disc
    shipping=Decimal('0')
    tax=r2((subtotal-discount)*Decimal('0'))
    total=subtotal-discount+shipping+tax
    return {k:str(r2(v)) for k,v in [('subtotal',subtotal),('discount',discount),('shipping',shipping),('tax',tax),('total',total)]}
