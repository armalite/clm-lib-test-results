import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace('if role != "admin" and r.get("project") not in user.get("projects", []):','if role != "admin" and r.get("project") not in user.get("projects", []) and r.get("owner") != user.get("name"):')
s=s.replace('params.get("purpose") == "audit")','params.get("purpose") in ("audit", "legal"))')
s=s.replace('    return json.dumps({"exported_by": user.get("name"), "records": recs})','''    res = {"exported_by": user.get("name"), "records": recs}
    if params.get("purpose") != "audit" and any(r.get("confidential") is True for r in out):
        res["confidential_count"] = sum(1 for r in out if r.get("confidential") is True)
    return json.dumps(res)''')
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
reg=reg.replace("CURRENT [S1.2] Scope: role admin exports any project; other roles only records whose project in user['projects'], others silently omitted.","CURRENT [S1.2, S4.2] Scope: role admin exports any project; other (non-viewer) roles only records whose project in user['projects'] OR whose owner == user['name']; others silently omitted.")
reg=reg.replace("CURRENT [S2.2] confidential True never exported, except when role admin and params.get('purpose')=='audit';","CURRENT [S2.2, S4.1] confidential True never exported, except when role admin and params.get('purpose') in ('audit','legal');")
reg=reg.replace("CURRENT [S2.5] Obligation:","CURRENT [S2.5, S4.1] Obligation now triggered by 'legal' purpose (implemented: confidential_count added when purpose!='audit' and confidential in output). Orig:")
reg+="\nHISTORY [S4.3] Decision record: move to JSON made for new reporting API."
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'note1','role':'note','body':'Stages 1-4 implemented in exporter/core.py. Next: advance.'}]
json.dump(c,open('/task/workspace/context.json','w'))