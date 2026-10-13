p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("import csv, io","import csv, io, json")
s=s.replace("        out.append(r)","        if params.get('since') is not None and str(r.get('created',''))[:10] < params['since']:\n            continue\n        out.append(r)")
i=s.index('    buf = io.StringIO()')
s=s[:i]+"    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': str(r['amount'])} for r in out]})\n"
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-600:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']=n['body'].replace('done through stage 2','done through stage 3')+"\nS3: params 'since' YYYY-MM-DD -> only created>=since. CHANGED format: json.dumps {'exported_by':name,'records':[{id int,title,owner,amount str}]} asc id (replaces CSV). Implemented."
json.dump({'format':'clm-context/v1','entries':[n]},open('/task/workspace/context.json','w'))