code='''"""Exporter implementation."""
import csv, io


def _filter(records, user, params):
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
    return sorted(out, key=lambda r: r['id'])


def export_records(records, user, params):
    params = params or {}
    recs = _filter(records, user, params)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in recs:
        w.writerow([int(r['id']), r['title'], r['owner'], r['amount']])
    return buf.getvalue()
'''
open('/task/workspace/exporter/core.py','w').write(code)
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(p.stderr[-1500:])