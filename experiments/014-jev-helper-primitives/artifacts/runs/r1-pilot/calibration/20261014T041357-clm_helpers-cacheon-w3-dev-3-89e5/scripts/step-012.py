import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    if role == 'viewer':\n        raise PermissionError('viewer')\n","")
s=s.replace("        if role != 'admin' and r.get('project')","        if role == 'viewer':\n            if r.get('owner') != user.get('name'):\n                continue\n        elif role != 'admin' and r.get('project')")
s=s.replace("params.get('purpose') == 'audit')","params.get('purpose') in ('audit', 'legal'))")
s=s.replace("    return json.dumps(doc)","    if params.get('purpose') == 'legal' and role == 'admin':\n        doc['confidential_count'] = sum(1 for r in out if r.get('confidential') is True)\n    return json.dumps(doc)")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
reg=reg.replace("CURRENT [S1.2] role viewer -> raise PermissionError.","HISTORY [S1.2] viewer used to raise PermissionError - replaced by S5.2.\nCURRENT [S5.2] viewer: no error; exports only records with owner==user['name'], any project; all other rules apply.")
reg=reg.replace("CURRENT [S1.5] confidential True never exported except role admin and params purpose=='audit'; other rules still apply.","CURRENT [S1.5, S5.1] confidential True never exported except role admin and params purpose in ('audit','legal'); other rules still apply.")
reg=reg.replace("number of confidential records in it.","number of confidential records in it. Triggered by S5.1 (legal): admin+purpose legal exports include confidential_count.")
reg+="\nHISTORY [S5.3] Decision: move to JSON made for new reporting API."
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'progress','role':'note','body':'Stages 1-5 implemented in exporter/core.py.'}]
json.dump(c,open('/task/workspace/context.json','w'))