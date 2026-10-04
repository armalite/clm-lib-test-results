import os
os.makedirs('/task/workspace/invoice',exist_ok=True)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice\n')
open('/task/workspace/invoice/core.py','w').write('''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal("0.01")
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
def compute_invoice(lines, customer):
    if not lines: raise ValueError("empty")
    sub=Decimal(0)
    for l in lines:
        q=l["qty"]
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError("qty")
        p=Decimal(str(l["unit_price"]))
        if p<0: raise ValueError("price")
        sub+=r(q*p)
    disc=Decimal(0)
    ship=Decimal(0)
    tax=r((sub-disc)*Decimal("0.10"))
    tot=sub-disc+ship+tax
    return {k:str(r(v)) for k,v in [("subtotal",sub),("discount",disc),("shipping",ship),("tax",tax),("total",tot)]}
''')
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])
open('/task/workspace/NOTES.md','w').write('stage1 done: core.py rounding/validation/tax10%\n')