"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def line_amount(line):
    q=int(line['qty'])
    amt=Decimal(q)*Decimal(str(line['unit_price']))
    if q>=200:
        amt*=Decimal('0.88')
    elif q>=50:
        amt*=Decimal('0.95')
    return amt

def discount_rate(subtotal, customer):
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))

def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        try:
            p=Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if not p.is_finite() or p<0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
    sub=sum((line_amount(l) for l in lines), Decimal('0'))
    disc=sub*discount_rate(sub, customer)
    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)
    s,d,t=r2(sub),r2(disc),r2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(r2(s-d+t))}

def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre:
        raise ValueError('bad currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+pre[currency]+str(abs(a))
