p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("'amount': r['amount']} for r in out], 'exported_by': user.get('name')}","'amount': r['amount'], 'project': r.get('project')} for r in out]}\n    if not admin:\n        obj['exported_by'] = user.get('name')")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-800:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]
b=reg['body']
b=b.replace("CURRENT [S2.4] Obligation: if format changes from CSV, every export in new format includes top-level 'exported_by'=user['name'].","CURRENT [S2.4, S7.2] Obligation: non-CSV exports include top-level 'exported_by'=user['name'], except role admin exports omit it (S7.2).\nHISTORY [S2.4] exported_by was required for all users incl admin.")
b=b.replace("CURRENT [S3.1, S1.1, S1.5, S2.4] Format: json.dumps object {'records':[{id int,title stripped,owner,amount str exact}] asc id, 'exported_by': user['name']}; no records -> empty list.","CURRENT [S3.1, S1.1, S1.5, S2.4, S7.1, S7.2] Format: json.dumps object {'records':[{id int,title stripped,owner,amount str exact,project (S7.1)}] asc id, 'exported_by': user['name'] (omitted for admin, S7.2)}; no records -> empty list.\nHISTORY [S3.1] records lacked project key.")
b+="\nHISTORY [S7.3] Decision: residency restriction lifted after regional data agreement signed."
reg['body']=b
c['entries']=[reg,{'id':'prog','role':'note','body':'Stages 1-7 implemented in exporter/core.py.'}]
json.dump(c,open('/task/workspace/context.json','w'))