p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("disc=r2(TIER.get(customer.get('tier'),Decimal(0))*sub)","elig=sum((a for a,l in zip(amts,lines) if l['qty']<100),Decimal(0))\n    disc=r2(TIER.get(customer.get('tier'),Decimal(0))*elig)")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' Stage4 done: tier eligible = sum of non-bulk line amts (var elig in compute_invoice). core.py: amts list, sub, disc, ship, tax, tot, returns dict of str.'
json.dump(c,open('/task/workspace/context.json','w'))