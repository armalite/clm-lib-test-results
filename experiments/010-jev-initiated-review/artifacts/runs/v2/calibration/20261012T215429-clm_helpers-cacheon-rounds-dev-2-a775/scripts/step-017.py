import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  n=0
  for i,l in enumerate(open(b+'logs/'+s),1):
    if re.search(r'ERROR|error|FAIL|fatal|429|OOM|expired',l,re.I) and 'slow query' not in l:
      n+=1
      if n<=3:print(s,i,l.rstrip()[:160])
  print(s,'count',n)