import re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  h=[i for i,l in enumerate(open(b+'logs/'+f),1) if re.search(r'429|cert_expired|ttl_s|validation',l)]
  print(f,h[:12])