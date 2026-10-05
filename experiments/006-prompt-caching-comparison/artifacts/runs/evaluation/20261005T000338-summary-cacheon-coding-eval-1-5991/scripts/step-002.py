code='''"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    subtotal=Decimal('0')
    for l in lines:
        amt=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=100: amt*=Decimal('0.90')
        subtotal+=r2(amt)
    discount=r2(subtotal*Decimal('0'))
    tax=r2((subtotal-discount)*Decimal('0.10'))
    total=subtotal-discount+tax
    return {k:str(r2(v)) for k,v in dict(subtotal=subtotal,discount=discount,tax=tax,total=total).items()}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','w').write('Stage1: line round half up, bulk qty>=100 x0.90, tax 10%, discount 0.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])