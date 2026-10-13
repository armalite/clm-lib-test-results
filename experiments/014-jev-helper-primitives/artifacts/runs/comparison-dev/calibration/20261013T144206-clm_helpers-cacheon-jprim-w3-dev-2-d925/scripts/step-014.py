import sys,subprocess
sys.path.insert(0,'/task/workspace')
import regtool
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    if role == 'viewer':\n        raise PermissionError('viewer')\n","")
s=s.replace("        if role != 'admin' and r.get('project')","        if role == 'viewer':\n            if r.get('owner') != user.get('name'):\n                continue\n        elif role != 'admin' and r.get('project')")
s=s.replace("params.get('include_archived') is True)","params.get('include_archived') is True and role == 'admin')")
s=s.replace("        out = out[:mx]","        out = out[:min(mx, 25)]")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])
c=regtool.load()
reg=[e for e in c['entries'] if e['id']=='register'][0]['body']
lines=reg.split('\n')
items={str(k):l for k,l in enumerate(lines) if l.startswith('CURRENT')}
new={'S5.1':'include_archived honoured only for role admin; other roles never get archived records.','S5.2':'Viewers no longer get an error; viewer exports only records they own, any project.','S5.3':'max_records above 25 treated as 25.'}
aff=regtool.affected(new,items);print({n:{k:v for k,v in d.items() if (v or 0)>0.5} for n,d in aff.items()})
rep={'CURRENT [S1.3]':"CURRENT [S1.3, S5.1] Status: only active; archived also included only if params include_archived is True AND role admin (other roles never archived).\nHISTORY [S1.3] Previously include_archived honoured for any role.",
'CURRENT [S2.1]':"CURRENT [S5.2] role viewer: no error; exports only records with owner==user['name'] in any project; all other rules apply.\nHISTORY [S2.1] Viewer used to raise PermissionError; replaced by S5.2.",
'CURRENT [S2.3]':"CURRENT [S2.3, S5.3] params max_records int>=1: only first N (ascending id) after all other rules; N above 25 treated as 25."}
out=[]
for l in lines:
    k=[x for x in rep if l.startswith(x)]
    out.append(rep[k[0]] if k else l)
regtool.set_entry(c,'register','\n'.join(out))
regtool.set_entry(c,'note1','Stages 1-5 implemented in exporter/core.py. Helper regtool.py (load,save,affected,set_entry). Next: advance.','note')
c['entries']=[e for e in c['entries'] if e['id'] in('register','note1')]
regtool.save(c)