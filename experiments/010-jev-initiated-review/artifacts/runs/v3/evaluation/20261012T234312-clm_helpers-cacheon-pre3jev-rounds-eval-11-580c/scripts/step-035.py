import os,re
b='/task/fixtures/round-09/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if 'INFO' not in l and 'slow query' not in l]
  print(f,len(h))
  for i,l in h[:3]+h[-1:]: print(i,l[:150])