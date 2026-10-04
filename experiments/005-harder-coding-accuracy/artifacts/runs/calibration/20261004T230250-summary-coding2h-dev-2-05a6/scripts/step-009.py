p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER.get(customer.get('tier'),Decimal(0))*subtotal)","TIER.get(customer.get('tier'),Decimal(0))*sum((a for a,l in zip(amounts,lines) if l['qty']<100),Decimal(0)))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done: tier eligible = non-bulk lines sum\n')
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(q.stderr[-1500:])