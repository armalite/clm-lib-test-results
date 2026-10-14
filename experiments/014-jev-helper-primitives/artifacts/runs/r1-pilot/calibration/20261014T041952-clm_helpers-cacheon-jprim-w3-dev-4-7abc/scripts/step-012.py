import sys,subprocess
p='/task/workspace/exporter/core.py';s=open(p).read()
s=s.replace('if role != "admin" and r.get("project") not in user.get("projects", []):','if role != "admin" and r.get("project") not in user.get("projects", []) and r.get("owner") != user.get("name"):')
s=s.replace('params.get("purpose") == "audit")','params.get("purpose") in ("audit", "regulator"))')
s=s.replace('''    return json.dumps({"records": recs, "exported_by": user.get("name")})''','''    res = {"records": recs, "exported_by": user.get("name")}
    if role == "admin" and params.get("purpose") == "regulator":
        res["confidential_count"] = sum(1 for r in out if r.get("confidential") is True)
    return json.dumps(res)''')
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])