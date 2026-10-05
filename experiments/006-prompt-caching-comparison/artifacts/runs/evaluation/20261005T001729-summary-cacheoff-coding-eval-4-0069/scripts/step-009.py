p='/task/workspace/invoice/core.py';s=open(p).read()
i=s.index('def compute_invoice');j=s.index('PREF = ')
new='''from decimal import ROUND_HALF_EVEN

def _e(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError("empty lines")
    for l in lines:
        q = l.get("qty")
        if not isinstance(q, int) or isinstance(q, bool) or q < 0:
            raise ValueError("bad qty")
        if Decimal(str(l["unit_price"])) < 0:
            raise ValueError("negative price")
    sub = Decimal("0")
    for l in lines:
        if l["qty"] == 0:
            continue
        amt = Decimal(l["qty"]) * Decimal(str(l["unit_price"]))
        if l["qty"] >= 200:
            amt *= Decimal("0.88")
        elif l["qty"] >= 50:
            amt *= Decimal("0.95")
        sub += amt
    disc = sub * TIER.get(customer.get("tier"), Decimal("0"))
    rate = Decimal("0.10")
    tax = (sub - disc) * rate
    if customer.get("tax_exempt") is True:
        tax = Decimal("0")
    rs, rd, rt = _e(sub), _e(disc), _e(tax)
    total = rs - rd + rt
    return {"subtotal": str(rs), "discount": str(rd), "tax": str(rt), "total": str(_e(total))}


'''
s=s[:i]+new+s[j:]
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])