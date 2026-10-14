import sys;sys.path.insert(0,'/task/workspace')
import regmaint
regmaint.update(7)
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace('"amount": r["amount"]}','"amount": r["amount"], "project": r.get("project")}')
s=s.replace('res = {"records": recs, "exported_by": user.get("name")}','res = {"records": recs}\n    if role != "admin":\n        res["exported_by"] = user.get("name")')
open(p,'w').write(s)
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
for e in regmaint.load()['entries']:
  if e['id'].startswith('reg.'):print(e['id'],e['body'][:90])