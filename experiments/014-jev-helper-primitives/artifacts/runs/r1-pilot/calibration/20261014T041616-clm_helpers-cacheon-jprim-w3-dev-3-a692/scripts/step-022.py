import subprocess,sys
p='exporter/core.py';s=open(p).read()
s=s.replace("        out = out[:mx]","        out = out[:min(mx, 30)]",1)
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])