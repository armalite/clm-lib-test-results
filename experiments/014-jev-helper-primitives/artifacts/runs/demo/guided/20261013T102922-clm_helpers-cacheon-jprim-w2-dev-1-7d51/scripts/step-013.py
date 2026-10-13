import subprocess,sys,json
sys.path.insert(0,'/task/workspace')
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    return json.dumps({'records'","    truncated = False\n    mr = params.get('max_records')\n    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1 and len(out) > mr:\n        out = out[:mr]; truncated = True\n    return json.dumps({'records'")
s=s.replace("'exported_by': user.get('name')})","'exported_by': user.get('name'), 'truncated': truncated})")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-400:])
import ctxhelper
req=open('/task/fixtures/stage-5/REQUIREMENTS.md').read()
print(ctxhelper.update(req,{'n.s5':"Stage5 done: params max_records int>=1 -> keep first N after all rules; JSON key 'truncated' bool (false if absent/no cut)."}))
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['role']=='note']
json.dump(c,open('/task/workspace/context.json','w'))
print([e['id'] for e in c['entries']])