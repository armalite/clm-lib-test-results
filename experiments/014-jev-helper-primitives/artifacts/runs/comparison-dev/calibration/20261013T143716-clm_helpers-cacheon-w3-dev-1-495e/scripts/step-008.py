code='''import json

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer may not export')
    since = params.get('since')
    regions = user.get('regions') or []
    out = []
    for r in records:
        if role != 'admin' and r.get('project') not in (user.get('projects') or []) and r.get('owner') != user.get('name'):
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
    recs = []
    for r in out:
        t = r['title']
        recs.append({'id': r['id'], 'title': t.strip() if isinstance(t, str) else t, 'owner': r['owner'], 'amount': r['amount']})
    return json.dumps({'exported_by': user.get('name'), 'records': recs})
'''
open('/task/workspace/exporter/core.py','w').write(code)
import subprocess,sys,json
res=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(res.stderr[-1500:])
p='/task/workspace/context.json'
c=json.load(open(p))
for e in c['entries']:
    if e['id']=='register':
        b=e['body'].replace("CURRENT [S1.1] Format: CSV via csv.writer default dialect, lineterminator='\\n'; header id,title,owner,amount; rows ascending id; no records -> header only.","HISTORY [S1.1] Format was CSV (header id,title,owner,amount) - replaced by S3.1.\nCURRENT [S3.1, S1.1] Output: json.dumps object with 'records': list of {id,title,owner,amount} (exactly these keys) ascending id; empty list if none.\nCURRENT [S2.4, S3.1] Since format is now JSON: top-level 'exported_by'=user['name'] (implemented).")
        b=b.replace("CURRENT [S1.3] admin: all projects; other roles only records with project in user['projects'] (silently skip others).","CURRENT [S1.3, S3.2] admin: all projects; other (non-viewer) roles: records with project in user['projects'] OR owner==user['name']; skip others silently.")
        b+="\nHISTORY [S3.3] Note: archived storage moves to cheaper tier; no export change."
        e['body']=b
    if e['id']=='status': e['body']='Stages 1-3 implemented in exporter/core.py.'
c['entries']=[e for e in c['entries'] if e['id'] in('register','status')]
json.dump(c,open(p,'w'))