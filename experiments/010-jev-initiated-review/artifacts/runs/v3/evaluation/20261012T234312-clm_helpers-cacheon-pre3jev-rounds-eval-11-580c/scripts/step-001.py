import os
r='/task/fixtures/round-01/'
for f in sorted(os.listdir(r)):print(f)
print(open(r+'board.md').read()[:1500])
for f in os.listdir(r+'logs'):
  L=open(r+'logs/'+f).read().splitlines()
  print(f,len(L))
  for i,l in enumerate(L,1):
    if 'ERROR' in l or 'WARN' in l: print(i,l[:150])