p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("discount=r(TIER.get(customer.get('tier'),Decimal('0'))*subtotal)","elig=sum((a for a,l in zip(amts,lines) if l['qty']<100),Decimal('0'))\n    discount=r(TIER.get(customer.get('tier'),Decimal('0'))*elig)")
open(p,'w').write(s)
import subprocess,sys,json
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(q.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+="\nStage4: tier-eligible = sum non-bulk line amts (elig var in compute_invoice). Implemented."
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))