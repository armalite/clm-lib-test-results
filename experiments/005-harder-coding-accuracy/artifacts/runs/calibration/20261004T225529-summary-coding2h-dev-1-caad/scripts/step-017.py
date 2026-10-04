p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("if q>=100:","if q>=50:")
s=s.replace("    ship=Decimal('7.50')","    c=Decimal(str(customer.get('coupon') or '0'))\n    disc=disc+max(Decimal(0),min(c,sub-disc))\n    ship=Decimal('7.50')")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('\nS7: bulk qty>=50; coupon=min(coupon,sub-tierdisc) added to discount.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])