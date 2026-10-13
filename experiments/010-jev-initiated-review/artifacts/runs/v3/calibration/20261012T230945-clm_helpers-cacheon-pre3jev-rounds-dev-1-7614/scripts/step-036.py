import re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  n=0
  for i,l in enumerate(open(b+'logs/'+s),1):
    if 'slow query' in l.lower():continue
    if re.search(r'error|fail|429|expire|pool|lag|mem|disk|dns|cert|inflight|stampede|miss',l,re.I):
      n+=1
      if n<=5:print(s,i,l.rstrip()[:150])
  print(s,'hits',n)