import os,re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[i for i,l in enumerate(L,1) if re.search('ERROR|heap|dns|429|cert|disk|pool|lag',l,re.I) and 'slow query' not in l]
  print(f,len(hits),hits[:20])
  if hits:print('  ',L[hits[0]-1])
  print(' first:',L[0])