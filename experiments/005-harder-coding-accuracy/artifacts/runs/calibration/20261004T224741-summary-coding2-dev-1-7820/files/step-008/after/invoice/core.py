from decimal import Decimal, ROUND_HALF_UP
Q=Decimal("0.01")
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
def compute_invoice(lines, customer):
    if not lines: raise ValueError("empty")
    sub=Decimal(0)
    elig=Decimal(0)
    for l in lines:
        q=l["qty"]
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError("qty")
        p=Decimal(str(l["unit_price"]))
        if p<0: raise ValueError("price")
        amt=q*p
        if q>=100: amt=amt*Decimal("0.90")
        sub+=r(amt)
        if q<100: elig+=r(amt)
    rate={"gold":Decimal("0.05"),"silver":Decimal("0.02")}.get(customer.get("tier"),Decimal(0))
    disc=r(elig*rate)
    ship=Decimal("7.50") if sub-disc<Decimal("100.00") else Decimal(0)
    trate={"NZ":Decimal("0.15"),"US":Decimal(0)}.get(customer.get("region"),Decimal("0.10"))
    tax=r((sub-disc)*trate)
    tot=sub-disc+ship+tax
    return {k:str(r(v)) for k,v in [("subtotal",sub),("discount",disc),("shipping",ship),("tax",tax),("total",tot)]}
