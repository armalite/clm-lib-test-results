import json,subprocess,sys
open('/task/workspace/exporter/core.py','w').write('''import csv, io


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
        if not (st == "active" or (st == "archived" and params.get("include_archived") is True)):
            continue
        since = params.get("since")
        if since is not None and r["created"] < since:
            continue
        if r.get("confidential") is True and not (role == "admin" and params.get("purpose") == "audit"):
            continue
        if r.get("region") == "eu" and "eu" not in (user.get("regions") or []):
            continue
        out.append(r)
    mx = params.get("max_records")
    if isinstance(mx, int) and mx >= 1:
        out = out[:mx]
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\\n")
    w.writerow(["id", "title", "owner", "amount"])
    for r in out:
        w.writerow([r["id"], r["title"].strip(), r["owner"], r["amount"]])
    return buf.getvalue()
''')
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']+'''
CURRENT [S2.1] role 'viewer' -> raise PermissionError, nothing exported.
CURRENT [S2.2] confidential True never exported, except when role admin and params.get('purpose')=='audit'; all other rules still apply to it.
CURRENT [S2.3] params 'max_records' int>=1: export only first N (ascending id) remaining after all other rules.
CURRENT [S2.4] Obligation: if format changes from CSV, every export in new format must include top-level "exported_by"=user['name'] (until withdrawn/changed).
CURRENT [S2.5] Obligation: if confidential records ever exported for purpose other than 'audit', export must include top-level "confidential_count" = number of confidential records in it.
CURRENT [S2.6] Residency: region 'eu' exported only if 'eu' in user['regions']; applies to admins too.'''
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'note1','role':'note','body':'Stages 1-2 implemented in exporter/core.py (filter loop + csv writer). Next: advance.'}]
json.dump(c,open('/task/workspace/context.json','w'))