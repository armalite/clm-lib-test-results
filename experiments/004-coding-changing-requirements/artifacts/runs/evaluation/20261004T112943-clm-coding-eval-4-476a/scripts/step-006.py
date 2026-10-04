p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
c=c.replace("Decimal('0'))\n    tot","Decimal('0.10'))\n    tot")
c=c.replace("    sub=Decimal('0')\n","    if not lines: raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')\n        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')\n    sub=Decimal('0')\n",1)
open(p,'w').write(c)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
import json
note='Stage1+2 done in invoice/core.py: Decimal r2 half-up per line, bulk qty>=100 x0.90, tiers platinum10 gold7 silver3, tax 10% on (sub-disc), validation ValueError (empty lines, qty non-positive-int, negative price). format_money stub (unspecified).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))