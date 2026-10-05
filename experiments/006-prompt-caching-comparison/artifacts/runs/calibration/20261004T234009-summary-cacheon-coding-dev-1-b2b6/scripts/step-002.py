code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price')))<0:
            raise ValueError('negative price')

def discount_rate(lines, customer, subtotal):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    _validate(lines)
    subtotal=sum((_r(l['qty']*Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    disc=_r(subtotal*discount_rate(lines,customer,subtotal))
    tax=_r((subtotal-disc)*tax_rate(customer))
    total=subtotal-disc+tax
    return {k:str(_r(v)) for k,v in (('subtotal',subtotal),('discount',disc),('tax',tax),('total',total))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','w').write('stage1 done: rounding per line, tax 10%, validation. core.py has discount_rate/tax_rate hooks.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])