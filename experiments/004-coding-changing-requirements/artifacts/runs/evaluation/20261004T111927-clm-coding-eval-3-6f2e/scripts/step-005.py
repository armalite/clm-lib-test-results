code='''from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q = Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def _ru(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}

def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    subtotal = sum((Decimal(str(l['qty'])) * Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
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
    return sign + PREFIX[currency] + str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-2 in invoice/core.py: compute_invoice exact sums, half-even round of subtotal/discount/tax, total from rounded. TIER dict gold .05 silver .02; tax_exempt True->0; tax_rate=0.10; format_money PREFIX (NZ$,A$,US$) half-up, neg sign before prefix, ValueError unknown.'}]},open('/task/workspace/context.json','w'))