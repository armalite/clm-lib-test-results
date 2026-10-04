import subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal("0.01")
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    if not lines: raise ValueError("empty lines")
    sub=Decimal(0)
    for l in lines:
        q=l.get("qty")
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError("bad qty")
        p=Decimal(str(l["unit_price"]))
        if p<0: raise ValueError("negative price")
        a=Decimal(q)*p
        if q>=200: a=a*Decimal("0.88")
        elif q>=50: a=a*Decimal("0.95")
        sub+=r2(a)
    disc=r2(sub*Decimal(0))
    tax=r2((sub-disc)*Decimal("0.10"))
    tot=sub-disc+tax
    return {"subtotal":str(r2(sub)),"discount":str(disc),"tax":str(tax),"total":str(r2(tot))}
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('Stage2 done: validation; bulk >=200 x0.88, >=50 x0.95.\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])