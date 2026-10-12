import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip())
import os
d='/task/fixtures/round-04/logs/'
for f in sorted(os.listdir(d)):
  for i,l in enumerate(open(d+f),1):
    if 'slow query' in l or 'INFO' in l or 'level=info' in l:continue
    print(f,i,l.rstrip()[:150])