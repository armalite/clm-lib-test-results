code='''import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer may not export')
    since = params.get('since')
    regions = user.get('regions') or []
    out = []
    for r in records:
        if role != 'admin' and r.get('project') not in (user.get('projects') or []):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if since is not None and str(r.get('created', ''))[:10] < since:
            continue
        if r.get('region') == 'ch' and 'ch' not in regions:
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
        t = r['title']
        w.writerow([r['id'], t.strip() if isinstance(t, str) else t, r['owner'], r['amount']])
    return buf.getvalue()
'''
open('/task/workspace/exporter/core.py','w').write(code)
import subprocess,sys,json
res=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(res.stderr[-1500:])
p='/task/workspace/context.json'
c=json.load(open(p))
for e in c['entries']:
    if e['id']=='register':
        e['body']+="\nCURRENT [S2.1] params 'since' YYYY-MM-DD: only records with created >= since.\nCURRENT [S2.2] region 'ch' exported only if 'ch' in user['regions'], admins too.\nCURRENT [S2.3] max_records int>=1: first N by ascending id after all other rules.\nCURRENT [S2.4] Obligation: if format ever changes from CSV, new format must include top-level 'exported_by'=user['name'].\nCURRENT [S2.5] title stripped of leading/trailing whitespace.\nCURRENT [S2.6] Obligation: if confidential records ever exported for purpose other than 'audit', export must include top-level 'confidential_count' (number of confidential records in it)."
    if e['id']=='status': e['body']='Stages 1-2 implemented in exporter/core.py.'
c['entries']=[e for e in c['entries'] if e['id'] in('register','status')]
json.dump(c,open(p,'w'))