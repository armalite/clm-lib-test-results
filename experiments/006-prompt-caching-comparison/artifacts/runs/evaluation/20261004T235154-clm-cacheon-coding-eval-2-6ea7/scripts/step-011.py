p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    tax = r2((subtotal - discount) * tax_rate(lines, customer))","    tax = r2((subtotal - discount) * tax_rate(lines, customer))\n    if customer.get('tax_exempt') is True:\n        tax = Decimal('0.00')")
s=s.replace("PREFIX[currency] + str(abs(a))","PREFIX[currency] + '{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])