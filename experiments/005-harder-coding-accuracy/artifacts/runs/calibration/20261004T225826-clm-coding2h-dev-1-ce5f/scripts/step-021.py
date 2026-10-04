p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("l['qty']>=100","l['qty']>=50").replace("l['qty']<100","l['qty']<50")
s=s.replace("    discount=sum(discounts,Decimal(0))\n","    discount=sum(discounts,Decimal(0))\n    coupon=Decimal(str((customer or {}).get('coupon') or 0))\n    discount=discount+max(Decimal(0),min(coupon,subtotal-discount))\n")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[{'id':'n1','role':'note','body':c['entries'][0]['body'].replace('Stages1-6','Stages1-7')+' Stage7: bulk qty>=50; coupon from customer applied min(coupon,subtotal-tierdisc) added to discount.'}]
json.dump(c,open('/task/workspace/context.json','w'))