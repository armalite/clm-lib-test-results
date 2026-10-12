import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):
    if l.strip(): print(f,i,l.rstrip())
from collections import defaultdict
for p in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  d=defaultdict(list)
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|FATAL|CRIT|SERVFAIL|429|refused|exhaust|OOM|expired|lag|disk|invalid',l) and 'slow query' not in l:
      k=re.sub(r'[\d:.TZ-]{6,}','',l)[:90].strip();d[k].append(i)
  for k,v in d.items(): print(p.split('/')[-1],v[:6],k)