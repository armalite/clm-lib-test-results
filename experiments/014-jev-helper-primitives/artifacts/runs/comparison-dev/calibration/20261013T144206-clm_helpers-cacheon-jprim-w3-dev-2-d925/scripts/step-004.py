import json,sys
sys.path.insert(0,'/task/workspace')
import regtool
open('/task/workspace/exporter/core.py','w').write('''import csv, io\n\ndef export_records(records, user, params):\n    params = params or {}\n    role = user.get('role')\n    if role == 'viewer':\n        raise PermissionError('viewer')\n    out = []\n    for r in records:\n        if role != 'admin' and r.get('project') not in user.get('projects', []):\n            continue\n        st = r.get('status')\n        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):\n            continue\n        since = params.get('since')\n        if since is not None and r.get('created', '') < since:\n            continue\n        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):\n            continue\n        if r.get('region') == 'eu' and 'eu' not in (user.get('regions') or []):\n            continue\n        out.append(r)\n    out.sort(key=lambda r: r['id'])\n    mx = params.get('max_records')\n    if isinstance(mx, int) and not isinstance(mx, bool) and mx >= 1:\n        out = out[:mx]\n    buf = io.StringIO()\n    w = csv.writer(buf, lineterminator='\\\\n')\n    w.writerow(['id', 'title', 'owner', 'amount'])\n    for r in out:\n        w.writerow([r['id'], r['title'].strip(), r['owner'], r['amount']])\n    return buf.getvalue()\n''')
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-600:])
c=regtool.load()
reg=[e for e in c['entries'] if e['id']=='register'][0]['body']
lines={l.split(']')[0]:l for l in reg.split('\n') if l.startswith(('CURRENT','HISTORY'))}
new={'S2.1':'viewer role raises PermissionError','S2.2':'confidential records never exported except admin with purpose audit','S2.6':'eu region records only if eu in user regions, admins too'}
print(regtool.affected(new,{k:v for k,v in lines.items()}))
reg+='''\nCURRENT [S2.1] role viewer -> raise PermissionError, nothing exported.
CURRENT [S2.2] confidential True never exported, except role admin AND params purpose=='audit'; other rules still apply.
CURRENT [S2.3] params max_records int>=1: only first N (ascending id) after all other rules.
CURRENT [S2.4] Obligation: if format changes from CSV, every export in new format includes top-level "exported_by"=user['name'].
CURRENT [S2.5] Obligation: if confidential records ever exported for purpose other than audit, export includes top-level "confidential_count".
CURRENT [S2.6] region 'eu' exported only if 'eu' in user['regions'] (admins too).'''
regtool.set_entry(c,'register',reg)
c['entries']=[e for e in c['entries'] if e['id']=='register']+[{'id':'note1','role':'note','body':'Stages 1-2 implemented in exporter/core.py, tests pass. Helper regtool.py (load,save,affected,set_entry). Next: advance.'}]
regtool.save(c)