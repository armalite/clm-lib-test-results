import re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'slow query' in l: continue
    if re.search('ERROR|WARN|FATAL|error',l): print(f,i,l.rstrip()[:160])