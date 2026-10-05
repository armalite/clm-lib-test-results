import os,re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[i for i,l in enumerate(L,1) if re.search('ERROR|WARN',l) and 'slow query' not in l]
  if hits:print(f,len(hits),hits[0],hits[-1],L[hits[0]-1][:200])
