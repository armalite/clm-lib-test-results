import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace('"amount": r["amount"]}','"amount": r["amount"], "project": r.get("project")}')
s=s.replace('    res = {"exported_by": user.get("name"), "records": recs}','    res = {"records": recs}\n    if role != "admin":\n        res["exported_by"] = user.get("name")')
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
lines=reg.split('\n')
nl=[]
for l in lines:
    if l.startswith('CURRENT [S2.4, S3.1]'):
        l="CURRENT [S2.4, S3.1, S7.2] Top-level exported_by=user['name'] in every export EXCEPT when role admin (admin exports omit it). Orig S2.4: if format changes from CSV, every export in new format must include exported_by."
    if l.startswith('CURRENT [S1.1, S3.1]'):
        l='CURRENT [S1.1, S3.1, S7.1] Format: json.dumps object with key "records": list of {id(int),title,owner,amount(str exactly as given),project} ascending id; no records -> empty list. Plus exported_by (non-admin).'
    nl.append(l)
nl.append('HISTORY [S7.3] Decision record: residency restriction lifted after regional data agreement signed.')
c['entries']=[{'id':'register','role':'summary','body':'\n'.join(nl)},{'id':'note1','role':'note','body':'All 7 stages implemented in exporter/core.py. Next: final.'}]
json.dump(c,open('/task/workspace/context.json','w'))