p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('ship=Decimal(0)','ship=Decimal("7.50") if sub-disc<Decimal("100.00") else Decimal(0)')
open(p,'w').write(s)
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(q.stderr[-1500:])
open('/task/workspace/NOTES.md','a').write('stage3 done: shipping 7.50 if sub-disc<100 untaxed\n')