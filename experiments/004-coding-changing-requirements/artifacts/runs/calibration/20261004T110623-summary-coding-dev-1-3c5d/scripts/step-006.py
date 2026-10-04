p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("        sub += r2(q * p)\n    disc = r2(sub * discount_rate(sub, customer))\n    tax = r2((sub - disc) * tax_rate(customer))\n    total = sub - disc + tax\n    return {'subtotal': str(r2(sub)), 'discount': str(disc), 'tax': str(tax), 'total': str(r2(total))}","        amt = q * p\n        if q >= 100:\n            amt = amt * Decimal('0.90')\n        sub += amt\n    disc = sub * discount_rate(sub, customer)\n    tax = (sub - disc) * tax_rate(customer)\n    rs, rd, rt = he(sub), he(disc), he(tax)\n    total = rs - rd + rt\n    return {'subtotal': str(rs), 'discount': str(rd), 'tax': str(rt), 'total': str(he(total))}")
s=s.replace("def discount_rate","def he(x):\n    return x.quantize(Q, rounding=ROUND_HALF_EVEN)\n\ndef discount_rate")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage3 done: bulk qty>=100 x0.9; exact calc, half-even rounding of sub/disc/tax.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])