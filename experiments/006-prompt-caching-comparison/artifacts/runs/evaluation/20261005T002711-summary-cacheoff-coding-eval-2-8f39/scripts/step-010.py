p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(lines, customer):\n    return Decimal('0.10')","def tax_rate(lines, customer):\n    if customer.get('tax_exempt') is True:\n        return Decimal('0')\n    return Decimal('0.10')")
s=s.replace("PREFIX[currency] + str(abs(a))","PREFIX[currency] + '{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done: tax_exempt, commas\n')
for k in ['tax_exempt',"{:,.2f}"]: print(k, k in s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])