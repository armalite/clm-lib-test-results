src='''"""Invoice implementation."""
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')
TIER_RATES = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}


def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def discount_rate(customer, subtotal):
    return TIER_RATES.get(customer.get('tier'), Decimal('0'))


def tax_rate(customer):
    return Decimal('0')


def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    subtotal = Decimal('0')
    for ln in lines:
        q = ln.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        p = Decimal(str(ln.get('unit_price')))
        if p < 0:
            raise ValueError('negative price')
        subtotal += r2(q * p)
    disc = r2(subtotal * discount_rate(customer, subtotal))
    tax = r2((subtotal - disc) * tax_rate(customer))
    total = subtotal - disc + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', disc), ('tax', tax), ('total', total))}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: invoice/core.py has compute_invoice (half-up line rounding, tier discount gold5/silver2 via discount_rate(customer,subtotal), tax_rate(customer)=0 hook, validation). format_money(amount,currency) stub NotImplemented.'}]},open('/task/workspace/context.json','w'))