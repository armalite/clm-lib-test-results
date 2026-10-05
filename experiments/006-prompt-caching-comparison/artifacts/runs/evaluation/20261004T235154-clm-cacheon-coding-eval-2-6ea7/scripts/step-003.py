code='''\"\"\"Invoice implementation.\"\"\"
from decimal import Decimal, ROUND_HALF_UP

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER_RATES = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}

def discount_rate(lines, customer, subtotal):
    return TIER_RATES.get(customer.get('tier'), Decimal('0'))

def tax_rate(lines, customer):
    return Decimal('0')

def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if not isinstance(q, int) or isinstance(q, bool) or q <= 0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price'))) < 0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
    subtotal = sum((r2(l['qty'] * Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    discount = r2(subtotal * discount_rate(lines, customer, subtotal))
    tax = r2((subtotal - discount) * tax_rate(lines, customer))
    total = subtotal - discount + tax
    return {k: str(r2(v)) for k, v in (('subtotal', subtotal), ('discount', discount), ('tax', tax), ('total', total))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: core.py has r2, TIER_RATES, discount_rate(lines,customer,subtotal), tax_rate(lines,customer)->0, validate, compute_invoice; format_money(amount,currency) stub NotImplemented (in __all__). Run tests after edits.'}]},open('/task/workspace/context.json','w'))