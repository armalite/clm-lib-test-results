import os
b='/task/fixtures/round-01/'
for f in sorted(os.listdir(b)):print(f)
print(open(b+'board.md').read()[:2000])
try:print(open(b+'changes.md').read()[:1500])
except Exception as e:print(e)
for f in sorted(os.listdir(b+'logs')):
 L=open(b+'logs/'+f).read().splitlines();print(f,len(L))
 for i,l in enumerate(L,1):
  if any(k in l for k in ('ERROR','WARN','error')):print(i,l[:160])