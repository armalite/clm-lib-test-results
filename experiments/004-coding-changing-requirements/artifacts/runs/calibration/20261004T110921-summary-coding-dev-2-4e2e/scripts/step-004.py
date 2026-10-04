p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer):\n    return Decimal('0')","def tax_rate(customer):\n    return Decimal('0.10')")
s=s.replace("PREFIX[currency]+str(abs(a))","PREFIX[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage2 done: tax 10%, commas in format_money\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])