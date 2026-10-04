p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    net=subtotal-discount\n","    c=customer.get('coupon')\n    c=Decimal(str(c)) if c not in (None,'') else Decimal('0')\n    discount=discount+r(max(Decimal('0'),min(c,subtotal-discount)))\n    net=subtotal-discount\n")
s=s.replace("tax=r(net*TAX","tax=r((net+shipping)*TAX")
open(p,'w').write(s)
import subprocess,sys,json
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(q.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+="\nStage7: coupon=min(coupon,subtotal-tier) added to discount; shipping taxed (net+shipping). Implemented."
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))