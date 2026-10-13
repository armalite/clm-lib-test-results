import re,glob
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
nz=re.compile(r'heartbeat|health ok|gc cycle|slow query|request ok')
for p in sorted(glob.glob(b+'logs/*.log')):
  n=p.split('/')[-1]
  for i,l in enumerate(open(p),1):
    if not nz.search(l):print(n,i,l.rstrip()[:150])