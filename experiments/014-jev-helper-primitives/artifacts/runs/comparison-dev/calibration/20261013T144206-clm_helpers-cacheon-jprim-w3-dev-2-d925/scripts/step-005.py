import re,sys,subprocess,json
p='/task/workspace/exporter/core.py'
s=open(p).read()
i=s.find('lineterminator=');print(repr(s[i:i+25]))
s=re.sub(r"lineterminator='[^']*'","lineterminator='\\\\n'",s)
open(p,'w').write(s)
i=s.find('lineterminator=');print(repr(s[i:i+25]))
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('register','note1')]
json.dump(c,open('/task/workspace/context.json','w'))