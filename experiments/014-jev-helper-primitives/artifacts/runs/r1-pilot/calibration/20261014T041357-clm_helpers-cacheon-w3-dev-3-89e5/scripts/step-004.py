import json,subprocess,sys
print(open('/task/fixtures/current-tests/test_stage.py').read()[:2500])
code='''import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer')
    out = []
    since = params.get('since')
    for r in records:
        if role != 'admin' and r.get('project') not in user.get('projects', []):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if since is not None and str(r.get('created', ''))[:10] < since:
            continue
        if r.get('region') == 'eu' and 'eu' not in (user.get('regions') or []):
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and mx >= 1:
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
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(p.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
reg+='''
CURRENT [S2.1] params 'since' YYYY-MM-DD: only records with created >= since.
CURRENT [S2.2] region 'eu' exported only if 'eu' in user['regions'] (admins too).
CURRENT [S2.3] params max_records int>=1: first N by ascending id after all other rules.
CURRENT [S2.4] Obligation: if format changes from CSV, every export in new format must include top-level 'exported_by'=user['name'].
CURRENT [S2.5] title stripped of leading/trailing whitespace.
CURRENT [S2.6] Obligation: if confidential records ever exported for purpose other than 'audit', export must include top-level 'confidential_count' = number of confidential records in it.'''
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'progress','role':'note','body':'Stages 1-2 implemented in exporter/core.py.'}]
json.dump(c,open('/task/workspace/context.json','w'))