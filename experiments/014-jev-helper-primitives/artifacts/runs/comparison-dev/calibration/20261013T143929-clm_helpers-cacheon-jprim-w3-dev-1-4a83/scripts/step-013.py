p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    if role == 'viewer':\n        raise PermissionError('viewer')\n","")
s=s.replace("        if role != 'admin' and r['project']","        if role == 'viewer':\n            if r.get('owner') != user.get('name'):\n                continue\n        elif role != 'admin' and r['project']")
s=s.replace("params.get('purpose') == 'audit')","params.get('purpose') in ('audit', 'litigation'))")
s=s.replace("    import json\n    return json.dumps({'exported_by': user.get('name'), 'records': [","    import json\n    res = {'exported_by': user.get('name')}\n    cc = sum(1 for r in out if r['confidential'] is True)\n    if cc and params.get('purpose') != 'audit':\n        res['confidential_count'] = cc\n    res['records'] = [")
s=s.replace("for r in out]})","for r in out]\n    return json.dumps(res)")
open(p,'w').write(s)
import sys;sys.path.insert(0,'/task/workspace')
import regmgr
c=regmgr.load()
c['entries']=[e for e in c['entries'] if e['id'] not in('s10.act','s10.obs','s10.rcpt','s11.act','s12.act','s12.obs','s8.obs')]
for e in c['entries']:
    if e['id']=='note.ctx': e['body']='Stage5 done: core.py implements all through S5.3. Helper regmgr.apply(c,new_items,amendments). Next: advance.'
regmgr.apply(c,[
('reg.S5.1','CURRENT [S5.1] confidential also exported when role admin and purpose==litigation (triggers S2.6 confidential_count).'),
('reg.S5.2','CURRENT [S5.2] viewers no longer error: export only records they own (owner==user name), any project; all other rules apply.'),
('reg.S5.3','HISTORY [S5.3] Decision: move to JSON made for new reporting API.')],{
'reg.S1.2':'HISTORY [S1.2] viewer -> PermissionError; replaced by S5.2.',
'reg.S1.5':'CURRENT [S1.5, S5.1] confidential True never exported except role admin and purpose in (audit, litigation); other rules still apply.',
'reg.S2.6':'CURRENT [S2.6, S5.1] Obligation (now triggered by litigation): if confidential records exported for purpose other than audit, top-level confidential_count = number of confidential records in export.'})
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])