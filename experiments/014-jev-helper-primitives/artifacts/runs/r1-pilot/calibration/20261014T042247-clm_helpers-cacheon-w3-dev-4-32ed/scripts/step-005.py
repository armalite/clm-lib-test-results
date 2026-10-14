code='''import csv, io


def export_records(records, user, params):
    params = params or {}
    if user.get('role') == 'viewer':
        raise PermissionError('viewer')
    out = []
    admin = user.get('role') == 'admin'
    projs = user.get('projects') or []
    regs = user.get('regions') or []
    inc = params.get('include_archived') is True
    since = params.get('since')
    audit = admin and params.get('purpose') == 'audit'
    for r in records:
        if not admin and r.get('project') not in projs:
            continue
        st = r.get('status')
        if not (st == 'active' or (inc and st == 'archived')):
            continue
        if since and r.get('created', '') < since:
            continue
        if r.get('confidential') is True and not audit:
            continue
        if r.get('region') == 'eu' and 'eu' not in regs:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and not isinstance(mx, bool) and mx >= 1:
        out = out[:mx]
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], str(r['title']).strip(), r['owner'], r['amount']])
    return buf.getvalue()
'''
open('/task/workspace/exporter/core.py','w').write(code)
import subprocess,sys,json
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(p.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=[e for e in c['entries'] if e['id']=='register'][0]
reg['body']+="\nCURRENT [S2.1] role 'viewer' -> raise PermissionError, nothing exported.\nCURRENT [S2.2] confidential True never exported, except role admin and params.get('purpose')=='audit'; other rules still apply.\nCURRENT [S2.3] params max_records int>=1: only first N (asc id) after all other rules.\nCURRENT [S2.4] Obligation: if format changes from CSV, every export in new format includes top-level 'exported_by'=user['name'].\nCURRENT [S2.5] Obligation: if confidential records exported for purpose other than 'audit', export includes top-level 'confidential_count' = number of confidential records in it.\nCURRENT [S2.6] region 'eu' exported only if 'eu' in user['regions'] (admins too)."
c['entries']=[reg,{'id':'prog','role':'note','body':'Stages 1-2 implemented in exporter/core.py.'}]
json.dump(c,open('/task/workspace/context.json','w'))