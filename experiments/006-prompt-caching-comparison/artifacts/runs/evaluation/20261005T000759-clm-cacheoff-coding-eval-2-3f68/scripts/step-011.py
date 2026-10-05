import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
print(s.split('\n')[45:52])
s=s.replace("def tax_rate(lines, customer):\n    return Decimal('0.10')","def tax_rate(lines, customer):\n    if customer.get('tax_exempt') is True:\n        return Decimal('0')\n    return Decimal('0.10')")
s=s.replace("str(abs(a))","'{:,.2f}'.format(_r(abs(Decimal(str(a)))))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])