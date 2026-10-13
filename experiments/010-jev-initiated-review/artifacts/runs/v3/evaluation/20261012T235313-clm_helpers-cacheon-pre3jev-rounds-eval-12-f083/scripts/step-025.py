import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip())
import os
d='/task/fixtures/round-06/logs/'
for f in sorted(os.listdir(d)):
  hits=[]
  for i,l in enumerate(open(d+f),1):
    if 'INFO' in l or 'slow' in l.lower():continue
    hits.append(i)
  print(f,hits)
  for i,l in enumerate(open(d+f),1):
    if i in hits[:2]:print(' ',i,l.rstrip()[:200])