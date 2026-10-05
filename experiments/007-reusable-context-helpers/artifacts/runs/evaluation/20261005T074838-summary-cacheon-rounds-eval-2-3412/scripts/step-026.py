import os
b='/task/fixtures/round-09/'
for i,l in enumerate(open(b+'board.md'),1):
  if l.strip(): print(i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  idx=[i for i,l in enumerate(L,1) if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l]
  print(f,len(idx),idx[:12])
  if idx: print('  ',L[idx[0]-1][:200])
