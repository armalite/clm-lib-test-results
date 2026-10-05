import re,json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("Decimal('0'))\n    tot","Decimal('0.10'))\n    tot")
s=s.replace("    sub=Decimal('0')\n","    if not lines:\n        raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if isinstance(q,bool) or not isinstance(q,int) or q<=0:\n            raise ValueError('qty')\n        if Decimal(str(l.get('unit_price')))<0:\n            raise ValueError('price')\n    sub=Decimal('0')\n")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'core.py: compute_invoice(lines,customer) _r half-up, bulk qty>=100 x0.90 per line, TIER platinum .10 gold .07 silver .03, tax 10% on (sub-disc), validation (empty lines, qty pos int, price>=0 -> ValueError). format_money unimplemented. Stage 2 applied; next: check test result then advance.'}]},open('/task/workspace/context.json','w'))