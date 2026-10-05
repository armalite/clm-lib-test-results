p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("sub = sum((Decimal(str(l['qty'])) * Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub = sum((line_amount(l) for l in lines), Decimal('0'))")
s=s.replace("def compute_invoice","def line_amount(l):\n    a = Decimal(str(l['qty'])) * Decimal(str(l['unit_price']))\n    if Decimal(str(l['qty'])) >= 100:\n        a = a * Decimal('0.90')\n    return a\n\ndef compute_invoice")
s=s.replace("str(abs(a))","'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1-3 in invoice/core.py: r2 half-even, line_amount (qty>=100 x0.90 unrounded), discount_rate(lines,customer,subtotal) tier gold5%/silver2%, tax_rate(customer)=0.10, tax_exempt is True->0, exact sub/disc/tax then round each; total=s-d+t. format_money PREFIX NZ$/A$/US$, -prefix, comma thousands, ValueError unknown. Tests /task/fixtures/current-tests.'}]},open('/task/workspace/context.json','w'))