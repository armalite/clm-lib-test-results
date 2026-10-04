p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("def tax_rate(customer):\n    return Decimal('0.10')","def tax_rate(customer):\n    if customer.get('tax_exempt') is True: return Decimal('0')\n    return Decimal('0.10')")
s=s.replace("def compute_invoice(lines, customer):\n","def compute_invoice(lines, customer):\n    if not lines: raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')\n        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')\n")
open(p,'w').write(s)
import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages 1-3 done in invoice/core.py: r2, TIER dict (platinum .10 gold .07 silver .03), tax_rate 0.10 (0 if tax_exempt is True), compute_invoice validates (empty lines, qty positive int, unit_price>=0 -> ValueError), format_money PFX dict NZ$/A$/US$ with {:,.2f}. Tests: unittest discover -s /task/fixtures/current-tests.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])