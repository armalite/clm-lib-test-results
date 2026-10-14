import sys,subprocess
p='/task/workspace/exporter/core.py';L=open(p).read().split('\n')
for i in range(18,25):print(i+1,L[i])
i=20
if 'region' in L[i] and 'continue' in L[i+1]:
  del L[i:i+2]
open(p,'w').write('\n'.join(L))
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-600:])