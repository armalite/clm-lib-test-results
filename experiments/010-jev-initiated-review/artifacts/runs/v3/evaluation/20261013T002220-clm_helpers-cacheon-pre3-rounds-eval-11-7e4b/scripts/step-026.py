import re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  bad=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|WARN|FATAL|error',l)]
  print(f,len(bad))
  for i,l in bad[:3]+bad[-1:]:print(' ',i,l[:150])