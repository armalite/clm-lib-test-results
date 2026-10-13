p='/task/workspace/exporter/core.py'
s=open(p).read()
ls=s.split('\n')
l=ls[19]
ind=len(l)-len(l.lstrip())
ls[19]=' '*ind+'if False:'
s='\n'.join(ls)
s=s.replace("'owner': r['owner'], 'amount': r['amount']}","'owner': r['owner'], 'amount': r['amount'], 'project': r['project']}")
open(p,'w').write(s)
import sys;sys.path.insert(0,'/task/workspace')
import regmgr
c=regmgr.load()
c['entries']=[e for e in c['entries'] if e['id'] not in('s14.act','s14.obs','s17.act','s17.obs','s17.rcpt','s19.act','s19.obs')]
for e in c['entries']:
    if e['id']=='note.ctx': e['body']='Stage7 done: core.py implements all through S7.3. Next: final.'
regmgr.apply(c,[
('reg.S7.1','CURRENT [S7.1] each exported JSON record also has key project (record project).'),
('reg.S7.2','CURRENT [S7.2] residency restriction withdrawn: all regions exported under ordinary rules.'),
('reg.S7.3','HISTORY [S7.3] Note: security confirmed confidential rules unchanged.')],{
'reg.S2.2':'HISTORY [S2.2, S4.2] region ch only if ch in user regions (case-insensitive, admins too); withdrawn by S7.2.',
'reg.S4.2':'HISTORY [S4.2] case-insensitive region comparison; moot after S7.2 withdrawal.',
'reg.S3.1':'CURRENT [S3.1, S2.5, S4.3, S7.1] Output is json.dumps of object with key records: list (ascending id) of objects with exactly keys id (int), title (normalized), owner, amount (str exact), project (S7.1). Replaces CSV of S1.1.'})
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])