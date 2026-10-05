code='''"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER_RATES = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}

def discount_rate(customer, subtotal):
    return TIER_RATES.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0')

def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if not isinstance(q, int) or isinstance(q, bool) or q <= 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(l.get('unit_price')))
        except InvalidOperation:
            raise ValueError('bad price')
        if p < 0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    _validate(lines)
    subtotal = sum((r2(l['qty'] * Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    discount = r2(subtotal * discount_rate(customer, subtotal))
    tax = r2((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {'subtotal': str(r2(subtotal)), 'discount': str(discount), 'tax': str(tax), 'total': str(r2(total))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','w').write('Stage1 done: rounding, tier discount gold5 silver2, validation. core.py has discount_rate/tax_rate hooks.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])