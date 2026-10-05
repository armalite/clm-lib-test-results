import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob(b+'logs/*.log')):
  L=open(p).read().splitlines();n=p.split('/')[-1]
  hits=[(i,l) for i,l in enumerate(L,1) if re.search(r'ERROR|WARN|429|disk|heap|cert|dns',l,re.I) and 'slow query' not in l]
  print(n,len(hits))
  for i,l in hits[:3]+hits[-2:]:print(' ',i,l[:150])