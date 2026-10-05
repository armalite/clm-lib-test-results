import re,glob
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|lag|restart|OOM|ttl',l,re.I):hits.append(i)
  print(f.split('/')[-1],len(hits),hits[:20])
  if hits:print(open(f).readlines()[hits[0]-1][:200])