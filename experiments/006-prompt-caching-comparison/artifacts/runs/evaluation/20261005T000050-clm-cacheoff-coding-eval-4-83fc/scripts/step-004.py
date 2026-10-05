import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("Decimal('0'))\n    tot","Decimal('0.10'))\n    tot")
s=s.replace("    sub=Decimal('0')\n","    if not lines: raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')\n        if Decimal(str(l['unit_price']))<0: raise ValueError('price')\n    sub=Decimal('0')\n",1)
open(p,'w').write(s)
print(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py: r2 half-up line rounding, bulk qty>=100 x0.90, tier platinum10/gold7/silver3%, tax 10% on (sub-disc), validation (empty lines, qty positive int, price>=0 -> ValueError). format_money unimplemented. Stage 2 released; implemented in step 4.'}]},open('/task/workspace/context.json','w'))