src='''"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

Q = Decimal('0.01')
TIER_RATES = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}


def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def discount_rate(customer, subtotal, lines):
    return TIER_RATES.get(customer.get('tier'), Decimal('0'))


def tax_rate(customer, lines):
    return Decimal('0')


def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub = Decimal('0')
    for ln in lines:
        q = ln.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(ln.get('unit_price')))
        except InvalidOperation:
            raise ValueError('bad price')
        if not p.is_finite() or p < 0:
            raise ValueError('bad price')
        sub += r2(q * p)
    disc = r2(sub * discount_rate(customer, sub, lines))
    tax = r2((sub - disc) * tax_rate(customer, lines))
    total = sub - disc + tax
    return {k: str(r2(v)) for k, v in (('subtotal', sub), ('discount', disc), ('tax', tax), ('total', total))}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: invoice/core.py has r2(), discount_rate(customer,sub,lines) tier gold5%/silver2%, tax_rate()=0, validation (empty, qty pos int, price>=0). format_money stub NotImplemented.'}]}
json.dump(c,open('/task/workspace/context.json','w'))