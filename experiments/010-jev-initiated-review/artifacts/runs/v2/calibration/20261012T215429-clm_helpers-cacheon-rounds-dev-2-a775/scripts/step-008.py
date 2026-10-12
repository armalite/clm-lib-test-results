import re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+s),1):
    if re.search('ERROR|error|FATAL|429|OOM|disk',l,re.I) and 'slow query' not in l: print(s,i,l.rstrip()[:160])