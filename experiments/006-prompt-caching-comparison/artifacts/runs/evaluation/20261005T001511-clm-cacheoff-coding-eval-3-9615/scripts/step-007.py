import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("sub=sum((int(l['qty'])*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))","sub=sum((_amt(l) for l in lines), Decimal('0'))")
s=s.replace("def compute_invoice","def _amt(l):\n    q=int(l['qty'])\n    a=q*Decimal(str(l['unit_price']))\n    if q>=100:\n        a=a*Decimal('0.90')\n    return a\n\ndef compute_invoice",1)
s=s.replace("return s+_P[currency]+str(abs(a))","return s+_P[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1-3 done in invoice/core.py: discount_rate tier gold 5%/silver 2%; tax_exempt True->tax 0; line amount _amt (qty>=100 x0.90); exact sums then half-even round (_b) of subtotal/discount/tax, total=sum of rounded; tax_rate(customer)=0.10; format_money (NZ$/A$/US$, -prefix, half-up _r, comma thousands, ValueError). Reqs at /task/fixtures/stage-N/REQUIREMENTS.md. Next: check test result then advance to stage 4.'}]}
json.dump(c,open('/task/workspace/context.json','w'))