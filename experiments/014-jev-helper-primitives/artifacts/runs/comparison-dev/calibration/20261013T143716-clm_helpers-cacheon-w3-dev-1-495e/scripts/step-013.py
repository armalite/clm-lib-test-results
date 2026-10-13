import subprocess,sys,json
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    if role == 'viewer':\n        raise PermissionError('viewer may not export')\n","")
s=s.replace("        if role != 'admin' and r.get('project')","        if role == 'viewer':\n            if r.get('owner') != user.get('name'):\n                continue\n        elif role != 'admin' and r.get('project')")
s=s.replace("params.get('purpose') == 'audit')","params.get('purpose') in ('audit', 'litigation'))")
s=s.replace("    return json.dumps({'exported_by': user.get('name'), 'records': recs})","    res = {'exported_by': user.get('name'), 'records': recs}\n    if role == 'admin' and params.get('purpose') == 'litigation':\n        res['confidential_count'] = sum(1 for r in out if r.get('confidential') is True)\n    return json.dumps(res)")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
cp='/task/workspace/context.json'
c=json.load(open(cp))
for e in c['entries']:
    if e['id']=='register':
        b=e['body']
        b=b.replace("CURRENT [S1.2] role 'viewer' -> raise PermissionError.","HISTORY [S1.2] viewer used to raise PermissionError - replaced by S5.2.\nCURRENT [S5.2, S1.2] viewer: no error; exports only records with owner==user['name'] in any project; all other rules apply.")
        b=b.replace("CURRENT [S1.5] confidential True never exported, except role admin and params.get('purpose')=='audit'; other rules still apply.","CURRENT [S1.5, S5.1] confidential True never exported, except role admin and purpose 'audit' or 'litigation'; other rules still apply.\nCURRENT [S2.6, S5.1] Since litigation exports confidential: admin+purpose litigation output includes top-level 'confidential_count' (implemented).")
        b+="\nHISTORY [S5.3] Decision: JSON move made for new reporting API."
        e['body']=b
    if e['id']=='status': e['body']='Stages 1-5 implemented in exporter/core.py.'
c['entries']=[e for e in c['entries'] if e['id'] in('register','status')]
json.dump(c,open(cp,'w'))