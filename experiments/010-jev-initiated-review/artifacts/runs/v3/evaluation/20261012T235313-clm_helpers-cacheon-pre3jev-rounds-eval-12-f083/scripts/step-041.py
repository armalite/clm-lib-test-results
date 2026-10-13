import re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  hits=[i for i,l in enumerate(open(b+'logs/'+f),1) if re.search(r'429|cert|config validation|ttl',l,re.I)]
  print(f,hits[:20])