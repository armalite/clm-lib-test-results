p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('    if q >= 100:\n        a = a * Decimal("0.90")\n','    if q >= 200:\n        a = a * Decimal("0.88")\n    elif q >= 50:\n        a = a * Decimal("0.95")\n')
s=s.replace('    return Decimal("0.10")','    return {"NZ": Decimal("0.15"), "AU": Decimal("0.10"), "US": Decimal("0")}.get(customer.get("region"), Decimal("0.12"))')
s=s.replace('def compute_invoice(lines, customer):\n','def _validate(lines):\n    if not lines:\n        raise ValueError("empty lines")\n    for l in lines:\n        q = l.get("qty")\n        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:\n            raise ValueError("bad qty")\n        try:\n            u = Decimal(str(l["unit_price"]))\n        except Exception:\n            raise ValueError("bad unit_price")\n        if not u.is_finite() or u < 0:\n            raise ValueError("negative unit_price")\n\n\ndef compute_invoice(lines, customer):\n    _validate(lines)\n')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('\nStage 4: validation, region tax, bulk 200->0.88/50->0.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])