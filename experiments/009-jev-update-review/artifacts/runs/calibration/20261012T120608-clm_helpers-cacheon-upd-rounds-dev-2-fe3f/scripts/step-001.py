import os
b='/task/fixtures/round-01/'
for f in sorted(os.listdir(b)):print(f)
print(open(b+'board.md').read()[:1500])
for f in os.listdir(b+'logs'):
  L=open(b+'logs/'+f).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l or 'WARN' in l]
  print(f,len(L),len(e));[print(i,l[:150]) for i,l in e[:4]]