p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('sub = sum((int(l["qty"]) * Decimal(str(l["unit_price"])) for l in lines), Decimal("0"))','sub = sum((_line(l) for l in lines), Decimal("0"))')
s=s.replace('def compute_invoice(','def _line(l):\n    q = int(l["qty"])\n    a = q * Decimal(str(l["unit_price"]))\n    if q >= 100:\n        a = a * Decimal("0.90")\n    return a\n\n\ndef compute_invoice(')
s=s.replace('{abs(a)}"','{abs(a):,.2f}"')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('\nStage 3: bulk qty>=100 x0.90 line; format_money comma thousands.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])