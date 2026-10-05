p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price']))*(Decimal('0.90') if Decimal(str(l['qty']))>=100 else 1) for l in lines), Decimal('0'))")
s=s.replace("PREFIX[currency]+str(abs(a))","PREFIX[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-3 in invoice/core.py: tax 10% (0 if tax_exempt is True); tier discount gold5%/silver2%; line amount qty*price, x0.90 if qty>=100; exact line amounts, round subtotal/discount/tax half-even, total=sum of rounded; format_money NZ$/A$/US$, comma thousands, ValueError else, -prefix negatives (half-even).'}]},open('/task/workspace/context.json','w'))