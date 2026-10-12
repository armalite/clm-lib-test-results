import os
b='/task/fixtures/round-01/'
for f in sorted(os.listdir(b)):print(f)
print(open(b+'board.md').read()[:1500])
import glob
for f in glob.glob(b+'logs/*'):
 L=open(f).read().splitlines();print(f,len(L));[print(i+1,l[:160]) for i,l in enumerate(L) if any(k in l for k in ('ERROR','WARN','error'))][:0]
 e=[(i+1,l[:150]) for i,l in enumerate(L) if 'ERROR' in l or 'WARN' in l][:4]
 for x in e:print(x)