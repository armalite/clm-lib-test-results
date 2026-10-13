import subprocess,sys
p='/task/workspace/exporter/core.py'
L=open(p).read().split('\n')
print(L[18:24])
if "region" in L[20]:
    nxt=L[21]
    print('next:',repr(nxt))
    if nxt.strip() in('continue','return False'):
        del L[20:22]
    else:
        del L[20]
    open(p,'w').write('\n'.join(L))
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])