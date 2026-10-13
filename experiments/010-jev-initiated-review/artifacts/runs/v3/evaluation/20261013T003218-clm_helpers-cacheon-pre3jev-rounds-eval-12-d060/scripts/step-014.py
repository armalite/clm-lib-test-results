import re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip()[:200])
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'ERROR|WARN|error|fail|expired|429|pool|lag|disk|memory|OOM|ttl',l): print(f,i,l.rstrip()[:150])