import subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
old="params.get('include_archived') is True and"
new="params.get('include_archived') is True and user.get('role') == 'admin' and"
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])