import json,subprocess,sys
open('/task/workspace/exporter/core.py','w').write('''import csv, io


def export_records(records, user, params):
    params = params or {}
    out = []
    for r in sorted(records, key=lambda r: r["id"]):
        if user.get("role") != "admin" and r.get("project") not in user.get("projects", []):
            continue
        st = r.get("status")
        if not (st == "active" or (st == "archived" and params.get("include_archived") is True)):
            continue
        since = params.get("since")
        if since is not None and r["created"] < since:
            continue
        out.append(r)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\\n")
    w.writerow(["id", "title", "owner", "amount"])
    for r in out:
        w.writerow([r["id"], r["title"].strip(), r["owner"], r["amount"]])
    return buf.getvalue()
''')
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])
reg='''CURRENT [S1.1] Format: CSV via csv.writer default dialect, lineterminator \\n; header id,title,owner,amount; one row per exported record ascending id; no records -> header only.
CURRENT [S1.2] Scope: role admin exports any project; other roles only records whose project in user['projects'], others silently omitted.
CURRENT [S1.3] Status: only 'active' exported unless params.get('include_archived') is True, then 'archived' too.
CURRENT [S1.4] Date filter: params 'since' YYYY-MM-DD -> only records with created >= since.
CURRENT [S1.5] Titles stripped of leading/trailing whitespace.
HISTORY [S1.6] Decision record: date filter introduced for monthly reconciliation runs.
CURRENT [S1.0] API export_records(records,user,params)->str; stdlib only; don't modify input; ignore unknown params; amount kept exactly as given; base: all records ascending id, values as given.'''
ctx={'format':'clm-context/v1','entries':[{'id':'register','role':'summary','body':reg},{'id':'note1','role':'note','body':'Stage 1 implemented in exporter/core.py (filter loop + csv writer). Next: advance.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))