import sys,subprocess;sys.path.insert(0,'/task/workspace')
import reghelper as h
reg={'S1.1':'CSV format header id,title,owner,amount sorted by id','S1.2':'scope by role/projects','S1.3':'confidential excluded unless admin audit'}
new={'S2.1':'only active status exported unless include_archived','S2.2':'if format changes from CSV, include exported_by','S2.3':'strip title whitespace'}
a=h.affected(reg,new);print(a)
p='/task/workspace/exporter/core.py';s=open(p).read()
s=s.replace("        if r.get('confidential')","        st = r.get('status')\n        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):\n            continue\n        if r.get('confidential')")
s=s.replace("r['title'], r['owner']","str(r['title']).strip(), r['owner']")
open(p,'w').write(s)
c=h.load()
c['entries']=[{'id':'s2.sum','role':'summary','body':'Stage1-2 done: exporter/core.py implements S1.1-1.3,S2.1,S2.3; reghelper.py has affected(reg,new) via jev and set_register(c,lines).'}]
h.set_register(c,['CURRENT [S1.1] Format: CSV via csv.writer default dialect, lineterminator \\n; header id,title,owner,amount; rows ascending id; no records -> header only.','CURRENT [S1.2] Scope: admin exports any project; other roles only records whose project in user[projects]; others silently omitted.','CURRENT [S1.3] Confidential records never exported, except when role admin and params purpose==audit; other rules still apply.','CURRENT [S2.1] Only status active exported, unless params include_archived is True, then archived too.','CURRENT [S2.2] Obligation: if format changes from CSV, every export in new format must include top-level field exported_by = user[name]; stays unless withdrawn/changed.','CURRENT [S2.3] Title exported with leading/trailing whitespace stripped.','HISTORY [S1.4] Decision record: CSV chosen for first release because finance imports into spreadsheets.'])
h.save(c)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-400:])