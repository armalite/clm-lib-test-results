p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("amounts=[r2(int(l['qty'])*Decimal(str(l['unit_price']))) for l in lines]","amounts=[r2(int(l['qty'])*Decimal(str(l['unit_price']))*(Decimal('0.90') if int(l['qty'])>=100 else 1)) for l in lines]")
s=s.replace("*Decimal('0'))\n    total","*Decimal('0.10'))\n    total")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: bulk qty>=100 x0.90 before rounding; tax 10% of sub-disc\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])