import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("params.get('purpose') == 'audit'","params.get('purpose') in ('audit','regulator')")
s=s.replace("    return json.dumps({'exported_by': user.get('name'), 'records': [","    obj = {'records': [")
s=s.replace("for r in out]})","for r in out]}\n    if not admin:\n        obj['exported_by'] = user.get('name')\n    return json.dumps(obj)")
open(p,'w').write(s)
print(s[-400:])
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s11.','s12.'))]
json.dump(c,open('/task/workspace/context.json','w'))