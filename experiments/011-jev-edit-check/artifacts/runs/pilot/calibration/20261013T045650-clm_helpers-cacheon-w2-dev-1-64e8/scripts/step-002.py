import json,subprocess,sys
open('/task/workspace/exporter/core.py','w').write('''import csv, io


def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer cannot export')
    out = []
    for r in records:
        if role != 'admin' and r['project'] not in user.get('projects', []):
            continue
        if r['status'] != 'active' and not (r['status'] == 'archived' and params.get('include_archived') is True):
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([int(r['id']), r['title'], r['owner'], r['amount']])
    return buf.getvalue()
''')
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(p.stderr[-1500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done in exporter/core.py: CSV header id,title,owner,amount via csv.writer lineterminator \\n, asc id; viewer->PermissionError; admin all projects, else project in user[projects]; only active unless params include_archived is True. Records: id,title,owner,project,status,amount(str),confidential,created.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))