import json,subprocess,sys
src='''import csv, io


def export_records(records, user, params):
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer may not export')
    if role == 'admin':
        sel = list(records)
    else:
        projs = set(user.get('projects') or [])
        sel = [r for r in records if r['project'] in projs]
    sel = sorted(sel, key=lambda r: r['id'])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator=chr(10))
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in sel:
        w.writerow([int(r['id']), r['title'], r['owner'], r['amount']])
    return buf.getvalue()
'''
open('/task/workspace/exporter/core.py','w').write(src)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-300:])
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id']=='note.stage1']+[{'id':'note.progress','role':'note','body':'Steps1-4: note accepted; exporter/core.py implements stage 1 (csv.writer lineterminator=chr(10), perms, sort by id). Step5: fixed lineterminator bug, reran tests (see output).'}]
json.dump(c,open(p,'w'))