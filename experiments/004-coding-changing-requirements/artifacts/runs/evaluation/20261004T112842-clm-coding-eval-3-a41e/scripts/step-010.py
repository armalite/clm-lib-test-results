p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace('''    return Decimal("0.10")''','''    return {"NZ": Decimal("0.15"), "AU": Decimal("0.10"), "US": Decimal(0)}.get((customer or {}).get("region"), Decimal("0.12"))''')
old='''    sub = sum((int(l["qty"]) * Decimal(str(l["unit_price"])) * (Decimal("0.90") if int(l["qty"]) >= 100 else 1) for l in lines), Decimal(0))'''
new='''    if not lines:
        raise ValueError("empty")
    sub = Decimal(0)
    for l in lines:
        q = l.get("qty")
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError("qty")
        up = Decimal(str(l["unit_price"]))
        if up < 0:
            raise ValueError("price")
        f = Decimal("0.88") if q >= 200 else Decimal("0.95") if q >= 50 else Decimal(1)
        sub += q * up * f'''
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])