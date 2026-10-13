import subprocess,sys,json
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("        out = out[:mx]","        out = out[:min(mx, 25)]")
s=s.replace("    res = {'exported_by': user.get('name'), 'records': recs}","    res = {'records': recs}\n    if role != 'admin':\n        res['exported_by'] = user.get('name')")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
cp='/task/workspace/context.json'
c=json.load(open(cp))
for e in c['entries']:
    if e['id']=='register':
        b=e['body']
        b=b.replace("CURRENT [S2.4, S3.1] Since format is now JSON: top-level 'exported_by'=user['name'] (implemented).","CURRENT [S2.4, S3.1, S6.1] JSON output includes top-level 'exported_by'=user['name'] for non-admin roles; admin exports omit it (S6.1).\nHISTORY [S2.4, S3.1] exported_by formerly required for all roles incl. admin - changed by S6.1.")
        b=b.replace("CURRENT [S2.3] max_records int>=1: first N by ascending id after all other rules.","CURRENT [S2.3, S6.2] max_records int>=1: first N by ascending id after all other rules; values above 25 treated as 25.")
        b=b.replace("CURRENT [S2.4] Obligation: if format ever changes from CSV, new format must include top-level 'exported_by'=user['name'].","HISTORY [S2.4] Obligation: if format changed from CSV, include top-level 'exported_by' (triggered by S3.1; admin exception by S6.1).")
        b+="\nHISTORY [S6.3] Note: web UI shows 50 records/page; no export change."
        e['body']=b
    if e['id']=='status': e['body']='Stages 1-6 implemented in exporter/core.py.'
c['entries']=[e for e in c['entries'] if e['id'] in('register','status')]
json.dump(c,open(cp,'w'))