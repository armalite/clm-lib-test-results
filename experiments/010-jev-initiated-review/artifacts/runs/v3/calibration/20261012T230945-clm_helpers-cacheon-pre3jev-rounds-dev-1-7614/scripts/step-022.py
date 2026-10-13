import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+s),1):
    if 'slow query' in l:continue
    if re.search(r'error|fail|429|expire|pool|lag|mem|disk|dns|cert|inflight|stampede|miss|ERROR',l,re.I):print(s,i,l.rstrip()[:150])