import re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
import os
for s in os.listdir(b+'logs'):
  for i,l in enumerate(open(b+'logs/'+s),1):
    if re.search('ERROR|429|fail|expired|OOM|lag|pool|inflight|SERVFAIL',l,re.I) and 'slow query' not in l:print(s,i,l.rstrip()[:150])