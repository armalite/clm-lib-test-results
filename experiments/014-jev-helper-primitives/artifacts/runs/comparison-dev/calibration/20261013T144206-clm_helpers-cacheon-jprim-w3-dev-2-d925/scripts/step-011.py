import sys,subprocess
sys.path.insert(0,'/task/workspace')
import regtool
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("if role != 'admin' and r.get('project') not in user.get('projects', []):","if role != 'admin' and r.get('project') not in user.get('projects', []) and r.get('owner') != user.get('name'):")
s=s.replace("params.get('purpose') == 'audit')","params.get('purpose') in ('audit', 'legal'))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])
c=regtool.load()
reg=[e for e in c['entries'] if e['id']=='register'][0]['body']
lines=reg.split('\n')
items={str(k):l for k,l in enumerate(lines) if l.startswith('CURRENT')}
new={'S4.1':'Confidential records may also be exported when role admin and purpose legal.','S4.2':'Non-admin non-viewer users may also export records they own (owner==user name) even outside their projects.'}
aff=regtool.affected(new,items);print({n:{k:v for k,v in d.items() if (v or 0)>0.5} for n,d in aff.items()})
out=[]
for l in lines:
    if l.startswith('CURRENT [S1.2]'):
        out.append("CURRENT [S1.2, S4.2] Scope: role admin exports any project; others only records with project in user projects OR owner==user['name'] (others silently omitted).\nHISTORY [S1.2] Previously project membership only.")
    elif l.startswith('CURRENT [S2.2]'):
        out.append("CURRENT [S2.2, S4.1] confidential True never exported, except role admin AND params purpose in ('audit','legal'); other rules still apply.\nHISTORY [S2.2] Previously audit only.")
    else: out.append(l)
out.append('HISTORY [S4.3] Decision record: move to JSON made for new reporting API.')
regtool.set_entry(c,'register','\n'.join(out))
regtool.set_entry(c,'note1','Stages 1-4 implemented in exporter/core.py. Helper regtool.py (load,save,affected,set_entry). Next: advance.','note')
c['entries']=[e for e in c['entries'] if e['id'] in('register','note1')]
regtool.save(c)