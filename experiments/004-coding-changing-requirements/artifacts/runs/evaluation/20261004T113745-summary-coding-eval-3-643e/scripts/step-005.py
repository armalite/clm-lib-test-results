src='''"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_EVEN

Q = Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}

def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return Decimal('0.10')

def compute_invoice(lines, customer):
    sub = sum((Decimal(l['qty']) * Decimal(l['unit_price']) for l in lines), Decimal('0'))
    disc = sub * discount_rate(lines, customer, sub)
    tax = (sub - disc) * tax_rate(customer)
    s, d, t = r2(sub), r2(disc), r2(tax)
    total = s - d + t
    return {'subtotal': str(s), 'discount': str(d), 'tax': str(t), 'total': str(r2(total))}

PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = Decimal(amount).quantize(Q)
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('stage2 done: tiers gold5/silver2, tax_exempt, half-even exact rounding.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])