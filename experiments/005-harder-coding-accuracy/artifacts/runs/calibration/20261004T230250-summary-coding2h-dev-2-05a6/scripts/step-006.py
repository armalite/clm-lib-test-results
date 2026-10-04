p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("amounts=[r(Decimal(l['qty'])*Decimal(str(l['unit_price']))) for l in lines]","amounts=[r(Decimal(l['qty'])*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=100 else 1)) for l in lines]")
s=s.replace("tax=r((subtotal-discount)*Decimal(0))","tax=r((subtotal-discount)*Decimal('0.10'))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: bulk qty>=100 x0.90 pre-round, tax 10%\n')
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(q.stderr[-1500:])