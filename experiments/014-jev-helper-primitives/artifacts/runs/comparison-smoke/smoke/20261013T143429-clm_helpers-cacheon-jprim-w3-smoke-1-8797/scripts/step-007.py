import sys,subprocess;sys.path.insert(0,'/task/workspace')
p='/task/workspace/exporter/core.py';s=open(p).read()
s=s.replace("if not admin and r.get('project') not in user.get('projects', []):","if not admin and r.get('project') not in user.get('projects', []) and not (user.get('role') not in ('admin','viewer') and r.get('owner') == user.get('name')):")
i=s.index('    buf = io.StringIO()');j=s.index('    return buf.getvalue()')+len('    return buf.getvalue()')
s=s[:i]+"    import json\n    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': str(r['title']).strip(), 'owner': r['owner'], 'amount': str(r['amount'])} for r in out]})"+s[j:]
open(p,'w').write(s)
h=open('/task/workspace/reghelper.py').read()
if 'def decide' not in h:
    h+='''
def decide(aff, thr=0.5):
    """returns {regid: [newids affecting it]} for probs>=thr"""
    d={}
    for nid,m in aff.items():
        for rid,pr in m.items():
            if pr is not None and pr>=thr: d.setdefault(rid,[]).append(nid)
    return d
'''
    open('/task/workspace/reghelper.py','w').write(h)
import importlib,reghelper as H;importlib.reload(H)
reg={'S1.1':'CSV format header id,title,owner,amount sorted by id','S1.2':'scope: admin any project; others only own projects','S1.3':'confidential excluded unless admin audit','S2.1':'only active unless include_archived','S2.2':'if format changes from CSV include exported_by','S2.3':'strip title'}
new={'S3.1':'Exports are now JSON with records list','S3.2':'non-admin non-viewer may export records they own outside projects'}
a=H.affected(reg,new);print(H.decide(a,0.4))
c=H.load()
c['entries']=[{'id':'s3.sum','role':'summary','body':'Stage1-3 done in exporter/core.py. reghelper.py: affected(reg,new) jev, decide(aff,thr), set_register, load/save.'}]
H.set_register(c,['CURRENT [S1.1, S3.1] Output: JSON text (json.dumps) object; key records = list of objects ascending id, keys exactly id(int),title,owner,amount(str as given). (CSV replaced.)','CURRENT [S2.2, S3.1] Format changed from CSV, so every export includes top-level exported_by = user[name].','CURRENT [S1.2, S3.2] Scope: admin any project; others only records whose project in user[projects], others silently omitted; except roles other than admin/viewer may also export records with owner==user[name] even outside projects.','CURRENT [S1.3] Confidential records never exported, except role admin and params purpose==audit; other rules still apply.','CURRENT [S2.1] Only status active exported, unless params include_archived is True, then archived too.','CURRENT [S2.3] Title stripped of leading/trailing whitespace.','HISTORY [S1.1] Was CSV csv.writer, lineterminator \\n, header id,title,owner,amount; replaced by S3.1.','HISTORY [S1.4] Decision: CSV chosen for first release because finance imports into spreadsheets.','HISTORY [S3.3] Note: archived project storage moves to cheaper tier; no export change.'])
H.save(c)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-600:])