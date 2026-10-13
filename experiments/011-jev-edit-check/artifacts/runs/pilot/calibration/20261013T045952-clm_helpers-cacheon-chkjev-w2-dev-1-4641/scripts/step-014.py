p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("if role != 'admin' and r['project'] not in user.get('projects', []):","if role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])