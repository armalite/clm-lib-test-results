from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    subtotal=Decimal('0')
    for l in lines:
        amt=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=100:
            amt*=Decimal('0.90')
        subtotal+=r2(amt)
    subtotal=r2(subtotal)
    discount=r2(subtotal*Decimal('0'))
    tax=r2((subtotal-discount)*Decimal('0.10'))
    total=subtotal-discount+tax
    return {'subtotal':str(subtotal),'discount':str(discount),'tax':str(tax),'total':str(r2(total))}


def format_money(amount, currency):
    raise NotImplementedError
