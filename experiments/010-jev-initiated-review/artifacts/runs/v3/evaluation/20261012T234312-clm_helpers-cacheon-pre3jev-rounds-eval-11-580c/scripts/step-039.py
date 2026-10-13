import re,glob
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if 'INFO' not in l and 'slow query' not in l]
  print(f.split('/')[-1],len(L))
  if L:print(' first',L[0]);print(' last',L[-1][0])