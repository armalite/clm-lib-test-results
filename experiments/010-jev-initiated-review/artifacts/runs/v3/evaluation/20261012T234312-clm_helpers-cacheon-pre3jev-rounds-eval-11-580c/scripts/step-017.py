import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):print(f,i,l.rstrip())
import os
d='/task/fixtures/round-05/logs/'
for f in sorted(os.listdir(d)):
  n=0
  for i,l in enumerate(open(d+f),1):
    if 'INFO' in l or 'slow query' in l:continue
    n+=1
    if n<=4:print(f,i,l.rstrip()[:150])
  print(f,'nonnoise',n)