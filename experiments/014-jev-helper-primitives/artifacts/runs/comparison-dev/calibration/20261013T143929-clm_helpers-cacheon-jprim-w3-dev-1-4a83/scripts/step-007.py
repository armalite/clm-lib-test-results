p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("if role != 'admin' and r['project'] not in user.get('projects', []):","if role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):")
i=s.index('    buf = io.StringIO()')
s=s[:i]+"""    import json
    return json.dumps({'exported_by': user.get('name'), 'records': [
        {'id': int(r['id']), 'title': r['title'].strip(), 'owner': r['owner'], 'amount': r['amount']} for r in out]})
"""
open(p,'w').write(s)
import sys;sys.path.insert(0,'/task/workspace')
import regmgr
c=regmgr.load()
c['entries']=[e for e in c['entries'] if e['id'] not in('s4.act','s4.obs','s4.rcpt','s5.act','s5.obs','s6.act','s6.obs')]
for e in c['entries']:
    if e['id']=='note.ctx': e['body']='Stage3 done: core.py implements all through S3.2 (JSON output with exported_by, owner access). Helper /task/workspace/regmgr.py: apply(c,new_items,amendments) uses jev to flag affected reg.* items. Register entries id reg.*.'
regmgr.apply(c,[
('reg.S3.1','CURRENT [S3.1, S2.5] Output is json.dumps of object with key records: list (ascending id) of objects with exactly keys id (int), title (stripped), owner, amount (str exact). Replaces CSV format of S1.1.'),
('reg.S3.2','CURRENT [S3.2] Non-admin non-viewer users may also export records they own (owner == user name) even outside their projects.'),
('reg.S3.3','HISTORY [S3.3] Note: archived project storage moves to cheaper tier; no export change.')],{
'reg.S1.1':'HISTORY [S1.1] CSV output header id,title,owner,amount, csv.writer \\n; replaced by JSON [S3.1]. CURRENT [S1.1] rows remain ascending id; no records -> empty records list.',
'reg.S1.3':'CURRENT [S1.3, S3.2] admin exports any project; others only records whose project in user projects, OR records they own (S3.2); silently drop others.',
'reg.S2.4':'CURRENT [S2.4, S3.1] Obligation now triggered (format changed to JSON): every export includes top-level field exported_by = user name.'})
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])