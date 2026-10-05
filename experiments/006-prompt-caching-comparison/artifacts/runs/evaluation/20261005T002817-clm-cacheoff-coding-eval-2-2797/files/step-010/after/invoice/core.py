from decimal import Decimal, ROUND_HALF_UP
Q=Decimal("0.01")
def r(x): return x.quantize(Q,rounding=ROUND_HALF_UP)
RATES={"platinum":Decimal("0.10"),"gold":Decimal("0.07"),"silver":Decimal("0.03")}
def compute_invoice(lines, customer):
    if not lines: raise ValueError("empty")
    sub=Decimal(0)
    for l in lines:
        q=l.get("qty")
        if not isinstance(q,int) or isinstance(q,bool) or q<0: raise ValueError("qty")
        p=Decimal(str(l["unit_price"]))
        if p<0: raise ValueError("price")
        if q==0: continue
        a=q*p
        if q>=100: a=a*Decimal("0.90")
        sub+=r(a)
    d=r(sub*RATES.get(customer.get("tier"),Decimal(0)))
    t=Decimal("0.00") if customer.get("tax_exempt") is True else r((sub-d)*Decimal("0.10"))
    return {"subtotal":str(r(sub)),"discount":str(d),"tax":str(t),"total":str(r(sub-d+t))}
PFX={"NZD":"NZ$","AUD":"A$","USD":"US$"}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError("currency")
    a=r(Decimal(str(amount)))
    return ("-" if a<0 else "")+PFX[currency]+"{:,.2f}".format(abs(a))
