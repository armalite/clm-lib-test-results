p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("params.get('include_archived') is True)","params.get('include_archived') is True and role == 'admin')")
s=s.replace("if r.get('region') == 'ch' and 'ch' not in (user.get('regions') or []):","if str(r.get('region') or '').lower() == 'ch' and 'ch' not in [str(x).lower() for x in (user.get('regions') or [])]:")
s=s.replace("'title': r['title'].strip()","'title': ' '.join(r['title'].split())")
open(p,'w').write(s)
import sys;sys.path.insert(0,'/task/workspace')
import regmgr
c=regmgr.load()
c['entries']=[e for e in c['entries'] if e['id'] not in('s7.act','s7.obs','s7.rcpt','s8.act','s9.act','s9.obs')]
for e in c['entries']:
    if e['id']=='note.ctx': e['body']='Stage4 done: core.py implements all through S4.3. Helper /task/workspace/regmgr.py: apply(c,new_items,amendments) uses jev to flag affected reg.* items. Register entries id reg.*. Next: advance.'
regmgr.apply(c,[
('reg.S4.1','CURRENT [S4.1] include_archived honoured only for role admin; other roles never get archived records.'),
('reg.S4.2','CURRENT [S4.2] region values compared case-insensitively (records and user regions).'),
('reg.S4.3','CURRENT [S4.3] titles: additionally collapse internal whitespace runs to single space.')],{
'reg.S1.4':'CURRENT [S1.4, S4.1] only status active; archived also included only if params include_archived is True AND role admin (S4.1).',
'reg.S2.2':'CURRENT [S2.2, S4.2] region ch (case-insensitive) exported only if ch in user regions (case-insensitive); applies to admins too.',
'reg.S2.5':'CURRENT [S2.5, S4.3] title exported stripped of leading/trailing whitespace and internal whitespace runs collapsed to one space.',
'reg.S3.1':'CURRENT [S3.1, S2.5, S4.3] Output is json.dumps of object with key records: list (ascending id) of objects with exactly keys id (int), title (normalized), owner, amount (str exact). Replaces CSV of S1.1.'})
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])