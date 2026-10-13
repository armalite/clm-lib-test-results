p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("        out.append(r)","        if r.get('status') != 'active' and not (params.get('include_archived') is True and r.get('status') == 'archived'):\n            continue\n        out.append(r)")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])