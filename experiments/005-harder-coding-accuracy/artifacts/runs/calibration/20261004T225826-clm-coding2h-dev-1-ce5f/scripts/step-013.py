import re,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines()):
    if 'gold' in l or 'silver' in l: print(i+1,l)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])