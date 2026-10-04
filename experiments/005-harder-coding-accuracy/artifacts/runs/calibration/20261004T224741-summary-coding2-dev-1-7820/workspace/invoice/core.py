from decimal import Decimal, ROUND_HALF_EVEN

def _q(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError("empty")
    sub=Decimal(0); elig=Decimal(0)
    for ln in lines:
        q=ln["qty"]
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError("qty")
        p=Decimal(str(ln["unit_price"]))
        if p<0: raise ValueError("price")
        amt=q*p
        if q>=100: amt=amt*Decimal("0.90")
        else: elig+=amt
        sub+=amt
    rate={"gold":Decimal("0.08"),"platinum":Decimal("0.10"),"silver":Decimal("0.02")}.get(customer.get("tier"),Decimal(0))
    disc=elig*rate
    ship=Decimal("7.50") if sub-disc<Decimal(100) else Decimal("0.00")
    trate={"NZ":Decimal("0.15"),"US":Decimal(0)}.get(customer.get("region"),Decimal("0.10"))
    tax=(sub-disc+ship)*trate
    rs,rd,rt=_q(sub),_q(disc),_q(tax)
    tot=rs-rd+ship+rt
    return {"subtotal":str(rs),"discount":str(rd),"shipping":str(_q(ship)),"tax":str(rt),"total":str(_q(tot))}
