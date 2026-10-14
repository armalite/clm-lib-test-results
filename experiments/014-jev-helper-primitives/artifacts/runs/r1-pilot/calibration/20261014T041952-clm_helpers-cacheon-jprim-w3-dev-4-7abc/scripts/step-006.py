import sys,subprocess;sys.path.insert(0,'/task/workspace')
src='''import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get("role")
    if role == "viewer":
        raise PermissionError("viewer")
    out = []
    for r in sorted(records, key=lambda r: r["id"]):
        if role != "admin" and r.get("project") not in user.get("projects", []):
            continue
        st = r.get("status")
        if st != "active" and not (st == "archived" and params.get("include_archived") is True):
            continue
        s = params.get("since")
        if s is not None and r["created"] < s:
            continue
        if r.get("confidential") is True and not (role == "admin" and params.get("purpose") == "audit"):
            continue
        if r.get("region") == "eu" and "eu" not in (user.get("regions") or []):
            continue
        out.append(r)
    m = params.get("max_records")
    if m is not None:
        out = out[:m]
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\\n")
    w.writerow(["id", "title", "owner", "amount"])
    for r in out:
        w.writerow([r["id"], r["title"].strip(), r["owner"], r["amount"]])
    return buf.getvalue()
'''
open('/task/workspace/exporter/core.py','w').write(src)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
import regmaint
c=regmaint.load();c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s3.','s4.','s5.'))]
for e in c['entries']:
  if e['id']=='n1':e['body']='Stage1+2 done: exporter/core.py implements S1.*,S2.* (S2.4/S2.5 dormant). Helper /task/workspace/regmaint.py: regmaint.update(N) per stage; override(eid,body,reason).'
regmaint.save(c)