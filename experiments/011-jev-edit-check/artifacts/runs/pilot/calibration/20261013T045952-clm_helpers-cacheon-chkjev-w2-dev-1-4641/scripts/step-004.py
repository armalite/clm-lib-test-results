p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("        out.append(r)","        if r['confidential'] is True and not (role == 'admin' and params.get('purpose') == 'audit'):\n            continue\n        if params.get('since') is not None and r['created'] < params['since']:\n            continue\n        out.append(r)")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])