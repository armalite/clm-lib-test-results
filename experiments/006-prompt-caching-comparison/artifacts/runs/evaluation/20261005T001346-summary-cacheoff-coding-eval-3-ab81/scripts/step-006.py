p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("sub = sum((int(l['qty']) * Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub = sum(((int(l['qty']) * Decimal(str(l['unit_price']))) * (Decimal('0.90') if int(l['qty']) >= 100 else 1) for l in lines), Decimal('0'))")
s=s.replace('{PREFIX[currency]}{abs(a)}','{PREFIX[currency]}{abs(a):,.2f}')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage3 done: bulk qty>=100 x0.90, format_money commas.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])