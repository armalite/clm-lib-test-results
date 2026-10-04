from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def _ru(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}

def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))

def _amt(l):
    q=Decimal(str(l['qty']))
    a=q*Decimal(str(l['unit_price']))
    if q>=200:
        a=a*Decimal('0.88')
    elif q>=50:
        a=a*Decimal('0.95')
    return a

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0:
            raise ValueError('price')
    subtotal = sum((_amt(l) for l in lines), Decimal('0'))
    discount = subtotal * discount_rate(lines, customer, subtotal)
    if customer.get('tax_exempt') is True:
        tax = Decimal('0')
    else:
        tax = (subtotal - discount) * tax_rate(customer)
    s, d, t = _r(subtotal), _r(discount), _r(tax)
    return {'subtotal': str(s), 'discount': str(d), 'tax': str(t), 'total': str(s - d + t)}

PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _ru(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + '{:,.2f}'.format(abs(a))
