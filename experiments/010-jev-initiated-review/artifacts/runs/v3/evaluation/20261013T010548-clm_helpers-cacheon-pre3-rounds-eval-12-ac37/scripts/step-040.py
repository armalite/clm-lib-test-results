import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in os.listdir(b+'logs'):
  L=open(b+'logs/'+f).read().splitlines()
  h=[i for i,l in enumerate(L,1) if re.search('ERROR|WARN|429|cert|ttl|fail',l)]
  if h:print(f,len(h),h[0],h[-1],L[h[0]-1][:150])