import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  hits=[i for i,l in enumerate(open(b+'logs/'+f),1) if re.search(r'WARN|ERROR|429|ttl|pool|exhaust',l) and 'slow query' not in l]
  print(f,len(hits),hits[:10])
  if hits:print(open(b+'logs/'+f).readlines()[hits[0]-1].rstrip()[:200])