p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    ship=Decimal(0)\n","    ship=Decimal('7.50') if sub-disc<Decimal('100.00') else Decimal(0)\n")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3: shipping 7.50 if sub-disc<100 else 0, untaxed\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])