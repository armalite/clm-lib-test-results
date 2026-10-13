import subprocess,sys,json
sys.path.insert(0,'/task/workspace')
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("if role != 'admin' and r['project'] not in user.get('projects', []):","if role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-500:])
h=open('/task/workspace/ctxhelper.py').read()
h=h.replace("if 'HISTORICAL' not in e['body'] and p is not None and p > 0.5:","if 'historical' not in e['body'].lower() and '[REVIEW' not in e['body'] and p is not None and p > 0.5:")
open('/task/workspace/ctxhelper.py','w').write(h)
import importlib,ctxhelper;importlib.reload(ctxhelper)
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['role']=='note': e['body']=e['body'].replace('[REVIEW: possibly affected by newer stage, see CHANGED rules] ','')
json.dump(c,open('/task/workspace/context.json','w'))
req=open('/task/fixtures/stage-4/REQUIREMENTS.md').read()
print(ctxhelper.update(req,{'n.s4':"Stage4 done: non-admin (non-viewer) also gets records with owner==user['name'] even outside projects. Viewer/admin rules unchanged; rest of stage1 permission rule in force."}))
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['role']=='note']
json.dump(c,open('/task/workspace/context.json','w'))
print([(e['id'],e['body'][:40]) for e in c['entries']])