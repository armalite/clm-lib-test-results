import re,glob
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob(b+'logs/*.log')):
  n=p.split('/')[-1]
  hits=[]
  for i,l in enumerate(open(p),1):
    if re.search(r'heartbeat|health|gc |\bok\b|slow query',l,re.I) and not re.search(r'ERROR|FATAL',l):continue
    hits.append((i,l.rstrip()[:150]))
  print(n,len(hits))
  for h in hits[:6]:print(' ',h)
  if len(hits)>6:print('  ... last',hits[-1][0])