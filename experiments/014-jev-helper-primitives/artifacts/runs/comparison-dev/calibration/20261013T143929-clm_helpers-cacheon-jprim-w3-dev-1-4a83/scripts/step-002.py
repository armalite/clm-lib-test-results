open('/task/workspace/exporter/core.py','w').write('''import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer')
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if role != 'admin' and r['project'] not in user.get('projects', []):
            continue
        st = r['status']
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        if r['confidential'] is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        out.append(r)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], r['title'], r['owner'], r['amount']])
    return buf.getvalue()
''')
open('/task/workspace/regmgr.py','w').write('''import json, clm_jev
P='/task/workspace/context.json'
def load(): return json.load(open(P))
def save(c): json.dump(c,open(P,'w'),indent=0)
def reg(c): return [e for e in c['entries'] if e['id'].startswith('reg.')]
def affected(new_text, c, thr=0.5):
    items={e['id']:e['body'] for e in reg(c) if e['body'].startswith('CURRENT')}
    if not items: return {}
    r=clm_jev.judge('Does the NEW change item modify, replace, conflict with or withdraw any part of this requirement?',items,background='NEW: '+new_text)
    a=r.get('answers') or {}
    return {k:v for k,v in a.items() if v is not None and v>=thr}
def apply(c, new_items, amendments):
    """new_items: list of (regid, body). amendments: regid -> new CURRENT body or 'HISTORY ...' text.
    Uses jev to flag affected items; prints flagged ones lacking an amendment."""
    for rid,body in new_items:
        if body.startswith('CURRENT') and '[S' in body and rid not in amendments:
            hits=affected(body,c)
            for k,p in hits.items():
                if k not in amendments: print('JEV FLAG',rid,'->',k,round(p,2))
    ents={e['id']:e for e in c['entries']}
    for k,b in amendments.items():
        if k in ents: ents[k]['body']=b
        else: c['entries'].append({'id':k,'role':'summary','body':b})
    for rid,body in new_items:
        if rid in ents: ents[rid]['body']=body
        else: c['entries'].append({'id':rid,'role':'summary','body':body})
    save(c)
''')
import sys;sys.path.insert(0,'/task/workspace')
import regmgr
c=regmgr.load()
c['entries']=[{'id':'note.ctx','role':'note','body':'Stage1 done: exporter/core.py implements S1.1-S1.5 (sorted by id, filters, csv). Helper /task/workspace/regmgr.py: apply(c,new_items,amendments) uses jev to flag affected reg.* items. Register entries id reg.*.'}]
regmgr.apply(c,[
('reg.api','CURRENT [S1.0] export_records(records,user,params)->str; records keys id,title,owner,project,status,amount(str, keep exact),confidential,created,region,optional updated; do not modify input; ignore unknown params; default all records ascending id.'),
('reg.S1.1','CURRENT [S1.1] CSV via csv.writer lineterminator \\n; header id,title,owner,amount; rows ascending id; no records -> header only.'),
('reg.S1.2','CURRENT [S1.2] role viewer -> raise PermissionError.'),
('reg.S1.3','CURRENT [S1.3] admin exports any project; others only records whose project in user projects (silently drop others).'),
('reg.S1.4','CURRENT [S1.4] only status active, unless params include_archived is True then archived too.'),
('reg.S1.5','CURRENT [S1.5] confidential True never exported except role admin and params purpose==audit; other rules still apply.'),
('reg.S1.6','HISTORY [S1.6] Decision: CSV chosen because finance imports into spreadsheets.')],{})
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])