p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('ROUND_HALF_UP','ROUND_HALF_EVEN')
s=s.replace("amounts=[r2(l['qty']*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=100 else 1))","amounts=[(l['qty']*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=100 else 1))")
s=s.replace("discount=sum((r2(d) for d in discounts),Decimal(0))","discount=sum(discounts,Decimal(0))")
s=s.replace("    tax=r2((subtotal-discount)*tax_rate(customer))\n    total=subtotal-discount+shipping+tax","    tax=(subtotal-discount+shipping)*tax_rate(customer)\n    subtotal,discount,tax=r2(subtotal),r2(discount),r2(tax)\n    total=subtotal-discount+shipping+tax")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[{'id':'n1','role':'note','body':c['entries'][0]['body'].replace('Stages1-5','Stages1-6')+' Stage6: no intermediate rounding, half-even final round of subtotal/discount/tax; tax on subtotal-discount+shipping.'}]
json.dump(c,open('/task/workspace/context.json','w'))