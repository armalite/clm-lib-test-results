import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):print(f,i,l.rstrip()[:200])
import os
d='/task/fixtures/round-05/logs/'
for s in sorted(os.listdir(d)):
  n=0
  for i,l in enumerate(open(d+s),1):
    if 'slow query' in l: continue
    if re.search(r'error|fail|429|expire|pool|lag|mem|disk|dns|cert|inflight|stampede|miss',l,re.I):
      n+=1
      if n<=4: print(s,i,l.rstrip()[:160])
  print(s,'hits',n)