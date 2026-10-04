code='''"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(subtotal, customer):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub = Decimal('0')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        p = Decimal(str(l['unit_price']))
        if p < 0:
            raise ValueError('negative price')
        sub += r2(q * p)
    disc = r2(sub * discount_rate(sub, customer))
    tax = r2((sub - disc) * tax_rate(customer))
    total = sub - disc + tax
    return {'subtotal': str(r2(sub)), 'discount': str(disc), 'tax': str(tax), 'total': str(r2(total))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','w').write('Stage1 done: rounding per line half-up, tax 10%, validation. core.py has discount_rate/tax_rate hooks.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])