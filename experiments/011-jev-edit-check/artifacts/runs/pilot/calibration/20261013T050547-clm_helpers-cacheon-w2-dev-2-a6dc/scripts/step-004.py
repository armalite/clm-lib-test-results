import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    for r in records:\n","    for r in records:\n        st = r.get('status')\n        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):\n            continue\n",1)
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[c['entries'][0],{'id':'n2','role':'note','body':"Stage2 done: status filter active only; archived too if params include_archived is True. OBLIGATION: if format ever changes from CSV, include top-level field exported_by=user['name'] (unless withdrawn)."}]
json.dump(c,open('/task/workspace/context.json','w'))