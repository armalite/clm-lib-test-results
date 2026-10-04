p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    subtotal=sum(amounts,Decimal('0'))\n    tier_disc=r2(TIER.get(customer.get('tier'),Decimal('0'))*subtotal)","    subtotal=sum(amounts,Decimal('0'))\n    eligible=sum((a for a,l in zip(amounts,lines) if int(l['qty'])<100),Decimal('0'))\n    tier_disc=r2(TIER.get(customer.get('tier'),Decimal('0'))*eligible)")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done: tier eligible = non-bulk lines\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])