import re,glob
from collections import defaultdict
for n in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+n),1): print(n,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  d=defaultdict(list)
  for i,l in enumerate(open(f),1):
    if re.search(r'WARN|ERROR|429|restart|OOM|cert|disk|heap',l,re.I) and 'slow query' not in l:
      m=re.sub(r'=\S+','=',l.split(None,3)[-1].strip())[:70]; d[m].append(i)
  for m,v in d.items(): print(f.split('/')[-1],v[0],v[-1],len(v),m)