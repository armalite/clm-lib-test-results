import re,glob
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
N=re.compile('heartbeat|health ok|gc cycle|slow query|request ok')
for p in sorted(glob.glob(b+'logs/*.log')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(p),1) if not N.search(l)]
  n=p.split('/')[-1]
  if L:print(n,len(L),L[0][0],L[-1][0],L[0][1][:150]);
  ks=set(re.sub(r'[0-9:T.\-Z]+','',x[1])[:80] for x in L);print(list(ks)[:4])