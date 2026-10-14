code='''import csv, io


def export_records(records, user, params):
    params = params or {}
    out = []
    admin = user.get('role') == 'admin'
    projs = user.get('projects') or []
    inc = params.get('include_archived') is True
    since = params.get('since')
    for r in records:
        if not admin and r.get('project') not in projs:
            continue
        st = r.get('status')
        if not (st == 'active' or (inc and st == 'archived')):
            continue
        if since and r.get('created', '') < since:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
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
c['entries']=[e for e in c['entries'] if e['id']=='register']
c['entries'].append({'id':'prog','role':'note','body':'Stage 1 implemented in exporter/core.py (filter then sort, csv writer).'})
json.dump(c,open('/task/workspace/context.json','w'))