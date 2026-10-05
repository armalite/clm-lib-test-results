src=open('/task/workspace/invoice/core.py').read()
src=src.replace("(Decimal('0.90') if int(l['qty'])>=100 else 1)","(Decimal('0.88') if int(l['qty'])>=200 else (Decimal('0.95') if int(l['qty'])>=50 else 1))")
src=src.replace("    return Decimal('0.10')\n","    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(customer.get('region'), Decimal('0.12'))\n")
src=src.replace("def compute_invoice(lines, customer):\n","def compute_invoice(lines, customer):\n    if not lines:\n        raise ValueError('empty')\n    for l in lines:\n        q = l.get('qty')\n        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:\n            raise ValueError('qty')\n        if Decimal(str(l['unit_price'])) < 0:\n            raise ValueError('price')\n")
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('Stage4 done: validation, region tax, bulk 200->.88 50->.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])