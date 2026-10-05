p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("    tax = r2((subtotal - discount) * tax_rate(customer))","    tax = r2((subtotal - discount) * tax_rate(customer))\n    if customer.get('tax_exempt') is True:\n        tax = Decimal('0.00')")
s=s.replace("str(abs(a))","'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage4 done: tax_exempt, comma format.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])