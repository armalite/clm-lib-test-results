p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price']))*(Decimal('0.90') if Decimal(str(l['qty']))>=100 else 1) for l in lines), Decimal('0'))")
c=c.replace("return s+PREFIX[currency]+str(abs(a))","return s+PREFIX[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(c)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py: stage1+2+3 done. exact sums, bulk qty>=100 line*0.90, half-even round of sub/disc/tax, total=s-d+t; discount_rate hook tier gold5/silver2; tax_exempt True->0; tax_rate hook 0.10; format_money NZ$/A$/US$, comma thousands, neg -prefix, else ValueError.'}]},open('/task/workspace/context.json','w'))