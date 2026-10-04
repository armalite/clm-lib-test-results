from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(subtotal, customer):
    t=(customer or {}).get('tier')
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(t,Decimal('0'))

def tax_rate(customer):
    cu=customer or {}
    if cu.get('tax_exempt') is True: return Decimal('0')
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(cu.get('region'),Decimal('0.12'))

def line_amount(l):
    a=Decimal(int(l['qty']))*Decimal(str(l['unit_price']))
    q=int(l['qty'])
    if q>=200: a*=Decimal('0.88')
    elif q>=50: a*=Decimal('0.95')
    return a

def validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        try: up=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('price')
        if up<0: raise ValueError('price')

def compute_invoice(lines, customer):
    validate(lines)
    sub=sum((line_amount(l) for l in lines), Decimal('0'))
    disc=sub*discount_rate(sub,customer)
    tax=(sub-disc)*tax_rate(customer)
    rs,rd,rt=(Decimal(x).quantize(Q,rounding=ROUND_HALF_EVEN) for x in (sub,disc,tax))
    tot=rs-rd+rt
    sub,disc,tax=rs,rd,rt
    return {k:str(v) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre: raise ValueError('bad currency')
    a=Decimal(str(amount)).quantize(Q,rounding=ROUND_HALF_EVEN)
    s='-' if a<0 else ''
    return s+pre[currency]+str(abs(a))
