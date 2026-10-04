p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("    return Decimal('0.10')\n","    return REGION.get(customer.get('region'), Decimal('0.12'))\n\nREGION = {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}\n",1)
s=s.replace("def compute_invoice(lines, customer):\n","def validate(lines):\n    if not lines:\n        raise ValueError('empty lines')\n    for l in lines:\n        q = l.get('qty')\n        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:\n            raise ValueError('bad qty')\n        try:\n            p = Decimal(str(l.get('unit_price')))\n        except Exception:\n            raise ValueError('bad price')\n        if not p.is_finite() or p < 0:\n            raise ValueError('negative price')\n\ndef compute_invoice(lines, customer):\n    validate(lines)\n")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done: validation, region tax, bulk tiers.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])