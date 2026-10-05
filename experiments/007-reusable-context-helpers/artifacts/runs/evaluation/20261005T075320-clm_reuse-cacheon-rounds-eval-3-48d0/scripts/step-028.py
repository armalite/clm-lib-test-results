import re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+s),1):
    if re.search(r'ERROR|WARN|429|heap|disk|cert',l,re.I) and 'slow query' not in l:print(s,i,l.rstrip()[:110])