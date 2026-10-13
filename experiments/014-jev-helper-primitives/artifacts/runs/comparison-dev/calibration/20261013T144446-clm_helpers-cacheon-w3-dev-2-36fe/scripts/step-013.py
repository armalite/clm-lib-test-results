import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace('''    if role == "viewer":
        raise PermissionError("viewer")
''','')
s=s.replace('''        if role != "admin" and r.get("project")''','''        if role == "viewer":
            if r.get("owner") != user.get("name"):
                continue
        elif role != "admin" and r.get("project")''')
s=s.replace('params.get("include_archived") is True))','params.get("include_archived") is True and role == "admin"))')
s=s.replace('        out = out[:mx]','        out = out[:min(mx, 25)]')
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
reg=reg.replace("CURRENT [S1.2, S4.2] Scope: role admin exports any project; other (non-viewer) roles","CURRENT [S1.2, S4.2, S5.2] Scope: role admin exports any project; viewer exports only records with owner == user['name'] (any project), all other rules apply; other roles")
reg=reg.replace("CURRENT [S1.3] Status: only 'active' exported unless params.get('include_archived') is True, then 'archived' too.","CURRENT [S1.3, S5.1] Status: only 'active' exported unless params.get('include_archived') is True AND role admin, then 'archived' too; non-admins never get archived.")
reg=reg.replace("CURRENT [S2.1] role 'viewer' -> raise PermissionError, nothing exported.","HISTORY [S2.1] viewer used to raise PermissionError; replaced by S5.2.")
reg=reg.replace("CURRENT [S2.3] params 'max_records' int>=1: export only first N","CURRENT [S2.3, S5.3] params 'max_records' int>=1 (values >25 treated as 25): export only first N")
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'note1','role':'note','body':'Stages 1-5 implemented in exporter/core.py. Next: advance.'}]
json.dump(c,open('/task/workspace/context.json','w'))