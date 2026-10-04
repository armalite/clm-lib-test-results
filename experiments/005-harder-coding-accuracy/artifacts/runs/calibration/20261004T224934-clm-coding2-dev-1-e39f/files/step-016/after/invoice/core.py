from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0); elig=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        a=q*p
        if q>=100: a=a*Decimal('0.90')
        sub+=a
        if q<100: elig+=a
    rate={'gold':Decimal('0.08'),'platinum':Decimal('0.10'),'silver':Decimal('0.02')}.get((customer or {}).get('tier'),Decimal(0))
    disc=elig*rate
    ship=Decimal('7.50') if sub-disc<Decimal('100.00') else Decimal('0.00')
    trate={'NZ':Decimal('0.15'),'US':Decimal(0)}.get((customer or {}).get('region'),Decimal('0.10'))
    tax=(sub-disc+ship)*trate
    sub,disc,tax=r2(sub),r2(disc),r2(tax)
    tot=sub-disc+ship+tax
    return {k:str(r2(v)) for k,v in dict(subtotal=sub,discount=disc,shipping=ship,tax=tax,total=tot).items()}
