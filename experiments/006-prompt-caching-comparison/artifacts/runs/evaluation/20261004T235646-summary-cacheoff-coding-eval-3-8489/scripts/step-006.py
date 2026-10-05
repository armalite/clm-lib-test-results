p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("sub=sum((int(l['qty'])*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub=sum((_line(l) for l in lines), Decimal('0'))")
c=c.replace("def compute_invoice(","def _line(l):\n    q=int(l['qty']); a=q*Decimal(str(l['unit_price']))\n    if q>=100: a=a*Decimal('0.90')\n    return a\n\ndef compute_invoice(")
c=c.replace('{abs(a)}"','{abs(a):,.2f}"')
open(p,'w').write(c)
open('/task/workspace/NOTES.md','a').write('Stage3 done: bulk qty>=100 x0.90 (exact), format_money commas.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])