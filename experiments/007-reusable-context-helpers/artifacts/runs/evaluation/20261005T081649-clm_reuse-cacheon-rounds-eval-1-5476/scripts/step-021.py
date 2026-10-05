import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(p).read().splitlines();hits=[i for i,l in enumerate(L,1) if re.search(r'ERROR|WARN|cert|lag|ttl|429|pool',l,re.I)]
  print(p.split('/')[-1],len(hits),hits[:3],hits[-1:] if hits else '')
  if hits:print(' ',L[hits[0]-1][:200])