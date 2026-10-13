import re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.strip()[:200])
import os
for s in sorted(os.listdir(b+'logs')):
  c=0
  for i,l in enumerate(open(b+'logs/'+s),1):
    if re.search(r'ERROR|WARN|error|warn',l) and 'slow query' not in l:
      c+=1
      if c<=6:print(s,i,l.strip()[:140])
  print(s,'count',c)