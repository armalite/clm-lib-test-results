import re,subprocess,sys,json
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("params.get('include_archived') is True)","params.get('include_archived') is True and role == 'admin')")
s=s.replace("regions = user.get('regions') or []","regions = [str(x).lower() for x in (user.get('regions') or [])]")
s=s.replace("if r.get('region') == 'ch' and","if str(r.get('region') or '').lower() == 'ch' and")
s=s.replace("t.strip() if isinstance(t, str)","' '.join(t.split()) if isinstance(t, str)")
open(p,'w').write(s)
res=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(res.stderr[-1500:])
cp='/task/workspace/context.json'
c=json.load(open(cp))
for e in c['entries']:
    if e['id']=='register':
        b=e['body']
        b=b.replace("CURRENT [S1.4] only status 'active' unless params.get('include_archived') is True (then archived too).","CURRENT [S1.4, S4.1] only status 'active' unless params.get('include_archived') is True AND role is 'admin' (then archived too); non-admins never get archived.\nHISTORY [S1.4] include_archived formerly honoured for any role - restricted by S4.1.")
        b=b.replace("CURRENT [S2.2] region 'ch' exported only if 'ch' in user['regions'], admins too.","CURRENT [S2.2, S4.2] region 'ch' exported only if 'ch' in user['regions'], admins too; region compare case-insensitive (records and user regions).")
        b=b.replace("CURRENT [S2.5] title stripped of leading/trailing whitespace.","CURRENT [S2.5, S4.3] title stripped of leading/trailing whitespace and every internal whitespace run replaced by single space.")
        e['body']=b
    if e['id']=='status': e['body']='Stages 1-4 implemented in exporter/core.py.'
c['entries']=[e for e in c['entries'] if e['id'] in('register','status')]
json.dump(c,open(cp,'w'))
print(s.count("role == 'admin')"),s.count('lower()'))