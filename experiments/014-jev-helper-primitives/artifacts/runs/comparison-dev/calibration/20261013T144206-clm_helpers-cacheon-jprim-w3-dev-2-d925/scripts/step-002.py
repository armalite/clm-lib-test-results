import json,os
os.makedirs('/task/workspace/exporter',exist_ok=True)
open('/task/workspace/exporter/core.py','w').write('''import csv, io

def export_records(records, user, params):
    params = params or {}
    out = []
    for r in records:
        if user.get('role') != 'admin' and r.get('project') not in user.get('projects', []):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        since = params.get('since')
        if since is not None and r.get('created', '') < since:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], r['title'].strip(), r['owner'], r['amount']])
    return buf.getvalue()
''')
open('/task/workspace/regtool.py','w').write('''import json, clm_jev
P='/task/workspace/context.json'
def load(): return json.load(open(P))
def save(c): json.dump(c,open(P,'w'))
def affected(new_items, register):
    """new_items: {id:text}; register: {regid:text}. returns {newid:{regid:prob}}"""
    res={}
    for nid,t in new_items.items():
        r=clm_jev.judge('Does this change notice modify, replace or withdraw the given register requirement? Notice: '+t, register)
        res[nid]=r.get('answers',{}) if r.get('status')=='ok' else {}
    return res
def set_entry(c,eid,body,role='summary'):
    c['entries']=[e for e in c['entries'] if e['id']!=eid]+[{'id':eid,'role':role,'body':body}]
''')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])
reg='''CURRENT [S1.1] Format: CSV via csv.writer default dialect, lineterminator \\n; header id,title,owner,amount; rows ascending id; no records -> header only.
CURRENT [S1.2] Scope: role admin exports any project; others only records with project in user projects (others silently omitted).
CURRENT [S1.3] Status: only active, unless params include_archived is True then archived too.
CURRENT [S1.4] Date filter: params since YYYY-MM-DD -> only created >= since.
CURRENT [S1.5] Titles stripped of leading/trailing whitespace.
HISTORY [S1.6] Decision record: date filter introduced for monthly reconciliation runs.
API: export_records(records,user,params)->str; don't mutate input; ignore unknown params; records fields id,title,owner,project,status,amount(str kept),confidential,created,region,[updated].'''
c={'format':'clm-context/v1','entries':[{'id':'register','role':'summary','body':reg},{'id':'note1','role':'note','body':'Stage1 implemented in exporter/core.py, tests pass. Helper /task/workspace/regtool.py (load,save,affected(new,register)->probs,set_entry). Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))