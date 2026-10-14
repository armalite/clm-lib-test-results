import reghelper,subprocess,sys
reghelper.update(7)
p='exporter/core.py';s=open(p).read()
s=s.replace("'amount': r['amount']}","'amount': r['amount'], 'project': r.get('project')}",1)
import re
for i,l in enumerate(s.splitlines()):
    if 'region' in l: print(i+1,l)
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])