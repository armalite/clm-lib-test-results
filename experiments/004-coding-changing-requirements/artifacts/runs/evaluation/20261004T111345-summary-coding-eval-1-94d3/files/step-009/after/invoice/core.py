from decimal import Decimal, ROUND_HALF_EVEN
Q=Decimal("0.01")
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
RATES={"gold":Decimal("0.05"),"silver":Decimal("0.02")}

def compute_invoice(lines, customer):
    if not lines: raise ValueError("empty lines")
    sub=Decimal(0)
    for l in lines:
        q=l.get("qty")
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError("bad qty")
        p=Decimal(str(l["unit_price"]))
        if p<0: raise ValueError("negative price")
        a=Decimal(q)*p
        if q>=200: a=a*Decimal("0.88")
        elif q>=50: a=a*Decimal("0.95")
        sub+=a
    disc=sub*RATES.get(customer.get("tier"),Decimal(0))
    TR={"NZ":Decimal("0.15"),"AU":Decimal("0.10"),"US":Decimal("0")}
    tax=(sub-disc)*TR.get(customer.get("region"),Decimal("0.12"))
    if customer.get("tax_exempt") is True: tax=Decimal(0)
    rs,rd,rt=r2(sub),r2(disc),r2(tax)
    return {"subtotal":str(rs),"discount":str(rd),"tax":str(rt),"total":str(rs-rd+rt)}

PREFIX={"NZD":"NZ$","AUD":"A$","USD":"US$"}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError("bad currency")
    d=r2(Decimal(str(amount)))
    s="-" if d<0 else ""
    return s+PREFIX[currency]+str(abs(d))
