p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("        out.append(r)","        if r['status'] != 'active' and not (r['status'] == 'archived' and params.get('include_archived') is True):\n            continue\n        out.append(r)")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-800:])
note='''REQS so far (impl in exporter/core.py, done through stage 2):
S1: export_records(records,user,params)->str. CSV via csv.writer lineterminator='\\n', header id,title,owner,amount, asc id, amount as given; empty->header only. viewer->PermissionError; admin all projects; others only project in user['projects']. confidential excluded unless admin and params.get('purpose')=='audit'. Ignore unknown params; don't mutate input.
S2: only status 'active' unless params.get('include_archived') is True. OBLIGATION: if format changes from CSV, new format must include top-level 'exported_by'=user['name'] (unless withdrawn).'''
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':note}]},open('/task/workspace/context.json','w'))