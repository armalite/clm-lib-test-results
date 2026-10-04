p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("sub = sum((Decimal(l['qty']) * Decimal(l['unit_price']) for l in lines), Decimal('0'))","sub = sum((line_amount(l) for l in lines), Decimal('0'))")
s=s.replace("def compute_invoice(","def line_amount(l):\n    a = Decimal(l['qty']) * Decimal(l['unit_price'])\n    if l['qty'] >= 100:\n        a = a * Decimal('0.90')\n    return a\n\ndef compute_invoice(")
s=s.replace("PREFIX[currency] + str(abs(a))","PREFIX[currency] + '{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: bulk qty>=100 x0.90 exact; format_money commas, half-up kept.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])