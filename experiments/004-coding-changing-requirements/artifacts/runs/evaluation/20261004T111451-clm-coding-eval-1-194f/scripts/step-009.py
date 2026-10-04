import re,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines()):
    if 'tax_rate' in l or 'format_money' in l or 'def ' in l: print(i+1,l)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])