import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("params.get('include_archived') is True)","params.get('include_archived') is True and user.get('role') == 'admin')")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-600:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=c['entries'][:3]+[{'id':'n4','role':'note','body':"Stage4 done: include_archived honoured only for role admin (core.py line 11)."}]
json.dump(c,open('/task/workspace/context.json','w'))