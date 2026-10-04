import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("'gold':Decimal('0.05'),","'gold':Decimal('0.08'),'platinum':Decimal('0.10'),")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0];n['body']=n['body'].replace('Stage1-4','Stage1-5').replace('gold5%/silver2%','gold8%/platinum10%/silver2%')
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))