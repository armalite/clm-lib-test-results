p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace('sub = sum((int(l["qty"]) * Decimal(str(l["unit_price"])) for l in lines), Decimal(0))','sub = sum((int(l["qty"]) * Decimal(str(l["unit_price"])) * (Decimal("0.90") if int(l["qty"]) >= 100 else 1) for l in lines), Decimal(0))')
s=s.replace('{abs(a)}"','{abs(a):,.2f}"')
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[{'id':'n1','role':'note','body':c['entries'][0]['body']+' Stage3 done: bulk qty>=100 line*0.90; format_money comma thousands.'}]
json.dump(c,open('/task/workspace/context.json','w'))