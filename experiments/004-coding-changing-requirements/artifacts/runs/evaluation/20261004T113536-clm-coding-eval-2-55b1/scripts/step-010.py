p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer, lines):\n    return Decimal('0.10')","def tax_rate(customer, lines):\n    if customer.get('tax_exempt') is True:\n        return Decimal('0')\n    return Decimal('0.10')")
s=s.replace("{abs(a):.2f}'","{abs(a):,.2f}'")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
print(s[s.find('def tax_rate'):s.find('def compute')])