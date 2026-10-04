import subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal("0.01")
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    sub=Decimal(0)
    for l in lines:
        a=Decimal(l["qty"])*Decimal(str(l["unit_price"]))
        if l["qty"]>=100: a=a*Decimal("0.90")
        sub+=r2(a)
    disc=r2(sub*Decimal(0))
    tax=r2((sub-disc)*Decimal("0.10"))
    tot=sub-disc+tax
    return {"subtotal":str(r2(sub)),"discount":str(disc),"tax":str(tax),"total":str(r2(tot))}
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice\n')
open('/task/workspace/NOTES.md','w').write('Stage1 done: half-up line rounding, tax 10%, bulk qty>=100 x0.90. impl in invoice/core.py\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])