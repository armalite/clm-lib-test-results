import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("(st == 'archived' and params.get('include_archived') is True)","(st == 'archived' and role == 'admin' and params.get('include_archived') is True)")
s=s.replace("if r.get('region') == 'eu' and 'eu' not in (user.get('regions') or []):","if str(r.get('region') or '').lower() == 'eu' and 'eu' not in [str(x).lower() for x in (user.get('regions') or [])]:")
s=s.replace("t.strip() if isinstance(t, str) else t","' '.join(t.split()) if isinstance(t, str) else t")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
reg=reg.replace("CURRENT [S1.4] only status active unless params include_archived is True (then archived too).","CURRENT [S1.4, S4.1] only status active; archived also exported only when params include_archived is True AND role admin; non-admin never get archived.")
reg=reg.replace("CURRENT [S2.2] region 'eu' exported only if 'eu' in user['regions'] (admins too).","CURRENT [S2.2, S4.2] region 'eu' exported only if 'eu' in user['regions'] (admins too); region compare case-insensitive in records and user regions.")
reg=reg.replace("CURRENT [S2.5] title stripped of leading/trailing whitespace.","CURRENT [S2.5, S4.3] title stripped of leading/trailing whitespace and every internal whitespace run replaced by single space.")
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'progress','role':'note','body':'Stages 1-4 implemented in exporter/core.py (single function export_records; JSON output incl exported_by).'}]
json.dump(c,open('/task/workspace/context.json','w'))
print(reg)