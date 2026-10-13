import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("            continue\n        out.append(r)","            continue\n        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):\n            continue\n        since = params.get('since')\n        if since is not None and str(r.get('created'))[:10] < since:\n            continue\n        out.append(r)")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done in exporter/core.py export_records(records,user,params): CSV header id,title,owner,amount via csv.writer lineterminator \\n, asc id; viewer->PermissionError; admin all projects, else project in user[projects]; only active unless params include_archived is True. Records: id,title,owner,project,status,amount(str),confidential,created.'},{'id':'n2','role':'note','body':'Stage2 done: confidential True excluded unless admin and purpose==audit; since YYYY-MM-DD filter created>=since (str compare [:10]). OBLIGATION: if format changes from CSV, add top-level exported_by=user[name] unless withdrawn.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))