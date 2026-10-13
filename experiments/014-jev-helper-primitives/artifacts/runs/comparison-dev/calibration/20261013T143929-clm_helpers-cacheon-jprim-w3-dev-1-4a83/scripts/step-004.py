import re
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("        out.append(r)","""        if params.get('since') is not None and str(r['created'])[:10] < params['since']:
            continue
        if r.get('region') == 'ch' and 'ch' not in (user.get('regions') or []):
            continue
        out.append(r)
    mr = params.get('max_records')
    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1:
        out = out[:mr]""")
s=s.replace("r['title'], r['owner']","r['title'].strip(), r['owner']")
open(p,'w').write(s)
import sys;sys.path.insert(0,'/task/workspace')
import regmgr
c=regmgr.load()
c['entries']=[e for e in c['entries'] if e['id'] not in('s2.act','s2.obs','s2.rcpt','s3.act','s3.obs')]
for e in c['entries']:
    if e['id']=='note.ctx': e['body']='Stage2 done: core.py implements S1.1-S1.5,S2.1-S2.5 (since, ch residency, max_records, title strip). Helper /task/workspace/regmgr.py: apply(c,new_items,amendments) uses jev to flag affected reg.* items. Register entries id reg.*.'
regmgr.apply(c,[
('reg.S2.1','CURRENT [S2.1] params since YYYY-MM-DD: only records with created on/after that date.'),
('reg.S2.2','CURRENT [S2.2] region ch exported only if ch in user regions; applies to admins too.'),
('reg.S2.3','CURRENT [S2.3] params max_records int>=1: only first N (ascending id) after all other rules.'),
('reg.S2.4','CURRENT [S2.4] Obligation: if format changes from CSV, every export in new format must include top-level field exported_by = user name. Until withdrawn/changed.'),
('reg.S2.5','CURRENT [S2.5] title exported with leading/trailing whitespace stripped.'),
('reg.S2.6','CURRENT [S2.6] Obligation: if confidential records ever exported for purpose other than audit, export must include top-level field confidential_count = number of confidential records in it.')],{})
import subprocess
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])