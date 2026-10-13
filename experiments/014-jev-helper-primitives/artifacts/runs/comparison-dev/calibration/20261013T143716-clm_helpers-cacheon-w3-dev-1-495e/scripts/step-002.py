import json,subprocess,sys
src='''import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer may not export')
    out = []
    for r in records:
        if role != 'admin' and r.get('project') not in user.get('projects', []):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], r['title'], r['owner'], r['amount']])
    return buf.getvalue()
'''
open('/task/workspace/exporter/core.py','w').write(src)
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(p.stderr[-1500:])
reg='''CURRENT [S1.1] Format: CSV via csv.writer default dialect, lineterminator='\\n'; header id,title,owner,amount; rows ascending id; no records -> header only.
CURRENT [S1.2] role 'viewer' -> raise PermissionError.
CURRENT [S1.3] admin: all projects; other roles only records with project in user['projects'] (silently skip others).
CURRENT [S1.4] only status 'active' unless params.get('include_archived') is True (then archived too).
CURRENT [S1.5] confidential True never exported, except role admin and params.get('purpose')=='audit'; other rules still apply.
HISTORY [S1.6] Decision: CSV chosen because finance imports into spreadsheets.
CURRENT [API] export_records(records,user,params)->str; don't modify input; ignore unknown params; fields exactly as given.'''
ctx={'format':'clm-context/v1','entries':[{'id':'register','role':'note','body':reg},{'id':'status','role':'note','body':'Stage 1 implemented in exporter/core.py (single function export_records). Tests run via unittest discover.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))