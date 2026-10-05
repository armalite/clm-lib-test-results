import json,subprocess,sys
p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price']))*(Decimal('0.90') if Decimal(str(l['qty']))>=100 else 1) for l in lines), Decimal('0'))")
c=c.replace("return s+PREFIX[currency]+str(abs(a))","return s+PREFIX[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(c)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py. Stage1: format_money PREFIX dict (NZ$,A$,US$), negative -> -prefix, unknown ValueError (half-up _r). Stage2: tier discount gold5%/silver2%; tax_exempt True -> tax 0; no line rounding, exact sub/disc/tax then half-even (_he) each, total=sum of rounded. tax 10%. Stage3 (done step7): qty>=100 line amount *0.90; format_money comma thousands via {:,.2f}. Tests: unittest discover -s /task/fixtures/current-tests.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))