p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer):\n    return Decimal('0.10')","def tax_rate(customer):\n    if customer.get('tax_exempt') is True: return Decimal('0')\n    return Decimal('0.10')")
s=s.replace("sign+PFX[currency]+str(abs(a))","sign+PFX[currency]+'{:,.2f}'.format(_r(abs(a)))")
open(p,'w').write(s)
print(s[s.find('def format_money'):])
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])