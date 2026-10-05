import re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search('ERROR|restart|OOM|429|cert|DNS|pool|lag|disk|backoff',l,re.I):print(f,i,l.rstrip()[:150])