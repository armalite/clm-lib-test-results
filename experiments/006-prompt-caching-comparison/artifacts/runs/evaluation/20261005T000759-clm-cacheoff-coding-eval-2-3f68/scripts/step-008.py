import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("q<=0:","q<0:")
s=s.replace("sub=sum((_r(l['qty']*Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))","sub=sum((_r(line_amount(l)) for l in lines if l['qty']!=0), Decimal('0'))")
s=s.replace("def compute_invoice","def line_amount(l):\n    a=l['qty']*Decimal(str(l['unit_price']))\n    if l['qty']>=100:\n        a=a*Decimal('0.90')\n    return a\n\ndef compute_invoice")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
n='Stages1-3 done in invoice/core.py: compute_invoice(lines,customer) -> dict of str subtotal/discount/tax/total. line_amount(l): qty*price, *0.90 if qty>=100, rounded half-up per line; qty 0 lines skipped. TIER platinum10/gold7/silver3%. tax_rate 10% on sub-disc. validate: nonempty, qty int >=0, price>=0. Hooks discount_rate(lines,customer,sub), tax_rate(lines,customer). format_money(amount,currency) PREFIX NZD NZ$/AUD A$/USD US$, -prefix negatives, ValueError else.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))