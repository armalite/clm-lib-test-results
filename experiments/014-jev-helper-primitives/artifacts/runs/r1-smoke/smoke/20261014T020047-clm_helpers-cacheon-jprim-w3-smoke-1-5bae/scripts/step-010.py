import subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("params.get('include_archived') is True)","params.get('include_archived') is True and user.get('role') == 'admin')")
s=s.replace("'title': str(r['title']).strip()","'title': ' '.join(str(r['title']).split())")
if 'import json' not in s: s='import json\n'+s
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])