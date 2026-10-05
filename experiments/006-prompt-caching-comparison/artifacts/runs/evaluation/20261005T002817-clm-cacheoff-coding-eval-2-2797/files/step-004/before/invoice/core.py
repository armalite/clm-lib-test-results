from decimal import Decimal, ROUND_HALF_UP
Q=Decimal("0.01")
def r(x): return x.quantize(Q,rounding=ROUND_HALF_UP)
RATES={"gold":Decimal("0.05"),"silver":Decimal("0.02")}
def compute_invoice(lines, customer):
    if not lines: raise ValueError("empty")
    sub=Decimal(0)
    for l in lines:
        q=l.get("qty")
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError("qty")
        p=Decimal(str(l["unit_price"]))
        if p<0: raise ValueError("price")
        sub+=r(q*p)
    d=r(sub*RATES.get(customer.get("tier"),Decimal(0)))
    t=r((sub-d)*Decimal(0))
    return {"subtotal":str(r(sub)),"discount":str(d),"tax":str(t),"total":str(r(sub-d+t))}
def format_money(amount, currency):
    raise NotImplementedError
