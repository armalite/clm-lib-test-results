open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice\n')
open('/task/workspace/invoice/core.py','w').write('''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
def compute_invoice(lines, customer):
    sub=Decimal(0)
    for l in lines:
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=100: a*=Decimal('0.90')
        sub+=r(a)
    disc=r(sub*Decimal(0))
    tax=r((sub-disc)*Decimal('0.10'))
    tot=sub-disc+tax
    return {'subtotal':str(r(sub)),'discount':str(disc),'tax':str(tax),'total':str(r(tot))}
''')
open('/task/workspace/NOTES.md','w').write('stage1 done: rounding per line half up, tax 10%, bulk qty>=100 x0.9\n')
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])