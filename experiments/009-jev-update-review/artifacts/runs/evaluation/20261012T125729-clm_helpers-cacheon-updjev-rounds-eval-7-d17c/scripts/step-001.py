import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f:print(r,x)
print(open(b+'board.md').read()[:1500])
import os
if os.path.exists(b+'changes.md'):print(open(b+'changes.md').read()[:1000])
for x in os.listdir(b+'logs'):
  L=open(b+'logs/'+x).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l or 'WARN' in l]
  print(x,len(L),e[:3])