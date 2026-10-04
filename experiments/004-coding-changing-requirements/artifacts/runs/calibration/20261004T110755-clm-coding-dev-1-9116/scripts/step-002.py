src='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        try:
            p=Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('bad price')
        if not p.is_finite() or p<0:
            raise ValueError('negative price')

def discount_rate(lines, customer, subtotal):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    _validate(lines)
    subtotal=sum((_r(l['qty']*Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    discount=_r(subtotal*discount_rate(lines,customer,subtotal))
    tax=_r((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+tax
    return {k:str(_r(v)) for k,v in [('subtotal',subtotal),('discount',discount),('tax',tax),('total',total)]}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])