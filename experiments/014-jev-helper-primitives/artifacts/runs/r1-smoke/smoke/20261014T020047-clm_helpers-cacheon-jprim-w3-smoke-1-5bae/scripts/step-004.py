import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("        out.append(r)","        st = r.get('status')\n        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):\n            continue\n        out.append(r)")
s=s.replace("r['title'], r['owner']","str(r['title']).strip(), r['owner']")
open(p,'w').write(s)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s2.','s3.'))]
for e in c['entries']:
    if e['id']=='n.state': e['body']='Stages 1-2 implemented in exporter/core.py; helper regtool.update(stage) maintains register (call once per stage).'
json.dump(c,open('/task/workspace/context.json','w'))
sys.path.insert(0,'/task/workspace')
import regtool; regtool.update(2)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-600:])