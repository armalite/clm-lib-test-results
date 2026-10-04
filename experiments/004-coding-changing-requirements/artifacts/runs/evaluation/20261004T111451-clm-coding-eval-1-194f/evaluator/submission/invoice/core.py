from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(lines, customer, subtotal):
    t=(customer or {}).get('tier')
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(t,Decimal('0'))

def r2e(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def tax_rate(customer):
    c=customer or {}
    if c.get('tax_exempt') is True: return Decimal('0')
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(c.get('region'),Decimal('0.12'))

def line_amount(line):
    q=line['qty']
    amt=Decimal(q)*Decimal(str(line['unit_price']))
    if q>=200:
        amt*=Decimal('0.88')
    elif q>=50:
        amt*=Decimal('0.95')
    return amt

def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        try:
            pr=Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('bad price')
        if not pr.is_finite() or pr<0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
    subtotal=sum((line_amount(l) for l in lines), Decimal('0'))
    discount=subtotal*discount_rate(lines,customer,subtotal)
    tax=(subtotal-discount)*tax_rate(customer)
    subtotal,discount,tax=r2e(subtotal),r2e(discount),r2e(tax)
    total=subtotal-discount+tax
    return {k:str(r2e(v)) for k,v in dict(subtotal=subtotal,discount=discount,tax=tax,total=total).items()}


def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre: raise ValueError('currency')
    d=r2(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+pre[currency]+str(abs(d))
