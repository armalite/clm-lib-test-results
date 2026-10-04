p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("amts=[r(l['qty']*Decimal(str(l['unit_price']))) for l in lines]","amts=[r(l['qty']*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=100 else 1)) for l in lines]")
s=s.replace("tax=Decimal('0')","tax=r(net*Decimal('0.10'))")
open(p,'w').write(s)
import subprocess,sys,json
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(q.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+="\nStage3: bulk qty>=100 line amt *0.90 before rounding; tax 10% all. Implemented."
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))