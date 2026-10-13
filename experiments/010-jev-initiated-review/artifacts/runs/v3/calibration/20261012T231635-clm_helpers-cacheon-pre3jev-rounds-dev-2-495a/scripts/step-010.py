import re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+s).read().splitlines()
  e=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|error|FATAL|fail|429|expired|OOM|backlog|lag|disk',l,re.I)]
  print(s,len(e))
  for i,l in e[:3]+e[-1:]:print(' ',i,l[:160])