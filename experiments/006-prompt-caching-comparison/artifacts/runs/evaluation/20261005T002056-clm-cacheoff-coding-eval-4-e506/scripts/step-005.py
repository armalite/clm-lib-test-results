import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("rate=Decimal(0)","rate=Decimal('0.10')")
s=s.replace("    sub=Decimal(0)\n","    if not lines: raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')\n        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')\n    sub=Decimal(0)\n",1)
s=s.replace("Decimal(l['unit_price'])","Decimal(str(l['unit_price']))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-2 implemented in invoice/core.py: compute_invoice(lines,customer) returns str dict subtotal/discount/tax/total; line round half-up, bulk qty>=100 x0.90; tiers platinum10/gold7/silver3%; tax 10% on (sub-disc); ValueError on empty lines, non-positive-int qty, negative price. format_money stub NotImplemented. Next: advance if tests OK.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))