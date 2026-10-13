import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
import os
d='/task/fixtures/round-08/logs/'
for s in sorted(os.listdir(d)):
  n=0
  for i,l in enumerate(open(d+s),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l.lower()) and 'slow query' not in l:
      n+=1
      if n<=3:print(s,i,l.rstrip()[:160])
  print(s,'count',n)