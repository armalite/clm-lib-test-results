p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("def tax_rate(customer):\n    return Decimal(0)","def tax_rate(customer):\n    return Decimal('0.10')")
s=s.replace("def compute_invoice(lines, customer):\n","def compute_invoice(lines, customer):\n    if not lines: raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')\n        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')\n")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 done in invoice/core.py: r2 half-up, line_amount bulk qty>=100 x0.90, TIER dict platinum10/gold7/silver3, tax_rate=0.10, compute_invoice validates (empty, qty positive int, price>=0 -> ValueError), returns str dict subtotal/discount/tax/total; format_money stub NotImplemented. Next: advance to stage 3.'}]},open('/task/workspace/context.json','w'))