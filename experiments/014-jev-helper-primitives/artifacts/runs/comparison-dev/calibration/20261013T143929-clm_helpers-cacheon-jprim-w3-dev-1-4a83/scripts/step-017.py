p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("        out = out[:mr]","        out = out[:min(mr, 25)]")
open(p,'w').write(s)
import sys;sys.path.insert(0,'/task/workspace')
import regmgr
c=regmgr.load()
c['entries']=[e for e in c['entries'] if e['id'] not in('s11.obs','s13.act','s13.obs','s13.rcpt','s15.act','s15.obs','s16.act','s16.obs')]
for e in c['entries']:
    if e['id']=='note.ctx': e['body']='Stage6 done: core.py implements all through S6.3. Helper regmgr.apply(c,new_items,amendments). Next: advance.'
regmgr.apply(c,[
('reg.S6.1','CURRENT [S6.1] exported_by omitted when role admin; still required for other roles.'),
('reg.S6.2','CURRENT [S6.2] max_records above 25 treated as 25.'),
('reg.S6.3','HISTORY [S6.3] Note: web UI shows 50 records/page; no export change.')],{
'reg.S2.4':'CURRENT [S2.4, S3.1, S6.1] every non-admin export includes top-level exported_by = user name; admin exports omit it (S6.1).',
'reg.S2.3':'CURRENT [S2.3, S6.2] params max_records int>=1: only first N (ascending id) after all other rules; N above 25 treated as 25.'})
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])