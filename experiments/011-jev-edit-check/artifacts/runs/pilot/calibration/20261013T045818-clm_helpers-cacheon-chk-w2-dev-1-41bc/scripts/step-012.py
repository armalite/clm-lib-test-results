p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("if role != 'admin' and r['project'] not in user.get('projects', []):","if role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):")
open(p,'w').write(s)
import subprocess,sys,json
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(q.stderr[-800:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace('Status: stages 1-3 implemented (core.py: _filter + export_records).','S4 CHANGED perms: non-admin also gets records with owner==user[name] even outside projects (viewer still PermissionError).\nStatus: stages 1-4 implemented (core.py: _filter + export_records).')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))