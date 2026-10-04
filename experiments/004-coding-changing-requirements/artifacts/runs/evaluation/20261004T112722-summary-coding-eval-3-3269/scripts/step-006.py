p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("sub=sum((Decimal(l['qty'])*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub=sum((Decimal(l['qty'])*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=100 else 1) for l in lines), Decimal('0'))")
c=c.replace("str(abs(a))\n","'{:,.2f}'.format(abs(a))\n")
open(p,'w').write(c)
open('/task/workspace/NOTES.md','a').write('Stage3 done: bulk qty>=100 x0.90, comma thousands in format_money.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])