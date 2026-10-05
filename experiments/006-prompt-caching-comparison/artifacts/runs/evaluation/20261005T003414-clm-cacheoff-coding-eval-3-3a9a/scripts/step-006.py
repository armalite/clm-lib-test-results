import json,subprocess,sys,re
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub=sum((_line(l) for l in lines), Decimal('0'))")
s=s.replace("def compute_invoice(","def _line(l):\n    q=Decimal(str(l['qty']))\n    a=q*Decimal(str(l['unit_price']))\n    if q>=100: a=a*Decimal('0.90')\n    return a\n\ndef compute_invoice(")
s=s.replace("PREFIX[currency]+str(abs(a))","PREFIX[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1-3 in core.py: compute_invoice exact (line amt, qty>=100 x0.90 via _line) then HALF_EVEN round s/d/t; tier gold5 silver2 (_discount_rate); tax_exempt True->0; tax 10%; format_money PREFIX NZ$/A$/US$ HALF_UP, comma thousands {:,.2f}, sign before prefix, ValueError unknown.'}]},open('/task/workspace/context.json','w'))