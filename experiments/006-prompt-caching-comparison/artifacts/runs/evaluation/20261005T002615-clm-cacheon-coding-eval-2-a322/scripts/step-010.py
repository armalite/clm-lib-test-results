p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    tax=r2((sub-disc)*taxrate)","    if customer.get('tax_exempt') is True: taxrate=Decimal(0)\n    tax=r2((sub-disc)*taxrate)")
s=s.replace("+str(abs(a))","+'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])