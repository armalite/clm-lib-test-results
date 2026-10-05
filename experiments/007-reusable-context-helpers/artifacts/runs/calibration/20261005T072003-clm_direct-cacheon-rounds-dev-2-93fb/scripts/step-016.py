import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-06/logs/*')):
  n=p.split('/')[-1];hits=[]
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|FATAL|SERVFAIL|cert|429|OOM|pool|disk|lag|invalid',l,re.I):hits.append(i)
  print(n,len(hits),hits[:3],hits[-1:] if hits else '')
  if hits:print(' ',open(p).read().splitlines()[hits[0]-1][:200])