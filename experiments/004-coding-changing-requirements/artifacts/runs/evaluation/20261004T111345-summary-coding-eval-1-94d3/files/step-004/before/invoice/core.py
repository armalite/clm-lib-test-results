from decimal import Decimal, ROUND_HALF_UP
Q=Decimal("0.01")
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    sub=Decimal(0)
    for l in lines:
        a=Decimal(l["qty"])*Decimal(str(l["unit_price"]))
        if l["qty"]>=100: a=a*Decimal("0.90")
        sub+=r2(a)
    disc=r2(sub*Decimal(0))
    tax=r2((sub-disc)*Decimal("0.10"))
    tot=sub-disc+tax
    return {"subtotal":str(r2(sub)),"discount":str(disc),"tax":str(tax),"total":str(r2(tot))}
