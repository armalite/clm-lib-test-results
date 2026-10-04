from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}
def tax_rate(customer, sub):
    return Decimal('0.10')
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')
        try: up=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('price')
        if not up.is_finite() or up<0: raise ValueError('price')
    sub=Decimal(0)
    for l in lines:
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200: a*=Decimal('0.88')
        elif l['qty']>=50: a*=Decimal('0.95')
        sub+=r(a)
    disc=r(sub*TIER.get(customer.get('tier'),Decimal(0)))
    tax=r((sub-disc)*tax_rate(customer, sub))
    tot=sub-disc+tax
    return {k:str(r(v)) for k,v in dict(subtotal=sub,discount=disc,tax=tax,total=tot).items()}

CUR={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in CUR: raise ValueError('currency')
    d=r(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+CUR[currency]+str(abs(d))
