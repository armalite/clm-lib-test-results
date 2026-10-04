p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.08'),")
s=s.replace("tax=r(net*Decimal('0.10'))","tax=r(net*TAX.get(customer.get('region'),Decimal('0.10')))")
s=s.replace("BULK=50\n","BULK=50\nTAX={'NZ':Decimal('0.15'),'US':Decimal('0')}\n")
open(p,'w').write(s)
import subprocess,sys,json
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(q.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+="\nStage6: TAX dict NZ 15% US 0% default 10%; TIER platinum 10% gold 8% silver 2%. Implemented (customer.get('region'))."
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))