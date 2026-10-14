p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    if user.get('role') == 'viewer':\n        raise PermissionError('viewer')\n","    viewer = user.get('role') == 'viewer'\n")
s=s.replace("inc = params.get('include_archived') is True","inc = admin and params.get('include_archived') is True")
s=s.replace("        if not admin and r.get('project')","        if viewer:\n            if r.get('owner') != user.get('name'):\n                continue\n        elif not admin and r.get('project')")
s=s.replace("        out = out[:mx]","        out = out[:min(mx, 20)]")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]
b=reg['body']
b=b.replace("CURRENT [S1.2, S4.2] Scope: role 'admin' any project; others (non-viewer)","CURRENT [S1.2, S4.2, S5.2] Scope: role 'admin' any project; viewer only records with owner==user['name'] any project (S5.2); others (non-viewer)")
b=b.replace("CURRENT [S1.3] Status: only 'active' unless params.get('include_archived') is True -> archived too.","CURRENT [S1.3, S5.1] Status: only 'active'; archived too only if role admin and params.get('include_archived') is True (S5.1); non-admin never archived.")
b=b.replace("CURRENT [S2.1] role 'viewer' -> raise PermissionError, nothing exported.","HISTORY [S2.1] viewer used to raise PermissionError; replaced by S5.2.")
b=b.replace("CURRENT [S2.3] params max_records int>=1: only first N (asc id) after all other rules.","CURRENT [S2.3, S5.3] params max_records int>=1: only first N (asc id) after all other rules; N>20 treated as 20 (S5.3).")
reg['body']=b
c['entries']=[reg,{'id':'prog','role':'note','body':'Stages 1-5 implemented in exporter/core.py (JSON output).'}]
json.dump(c,open('/task/workspace/context.json','w'))