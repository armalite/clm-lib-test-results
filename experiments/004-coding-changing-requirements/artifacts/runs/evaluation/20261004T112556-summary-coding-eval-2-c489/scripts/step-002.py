import subprocess,sys
print(open('/task/workspace/invoice/__init__.py').read());print(open('/task/workspace/invoice/core.py').read())
code='''from decimal import Decimal, ROUND_HALF_UP

Q = Decimal("0.01")
TIER = {"gold": Decimal("0.05"), "silver": Decimal("0.02")}

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError("empty")
    sub = Decimal(0)
    for l in lines:
        q = l.get("qty")
        if not isinstance(q, int) or isinstance(q, bool) or q <= 0:
            raise ValueError("qty")
        p = Decimal(str(l["unit_price"]))
        if p < 0:
            raise ValueError("price")
        sub += r2(q * p)
    disc = r2(sub * TIER.get(customer.get("tier"), Decimal(0)))
    tax = r2((sub - disc) * Decimal(0))
    total = sub - disc + tax
    return {"subtotal": str(r2(sub)), "discount": str(disc), "tax": str(tax), "total": str(r2(total))}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice\n')
open('/task/workspace/NOTES.md','w').write('stage1 done: rounding, tier gold5 silver2, validation. tax rate 0.\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])