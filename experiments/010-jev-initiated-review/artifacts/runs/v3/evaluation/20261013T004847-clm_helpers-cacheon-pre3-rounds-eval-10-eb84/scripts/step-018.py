import os
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import re
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  bad=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|FATAL|error|429|SERVFAIL|pool|OOM|disk|lag',l)]
  print(f,len(bad),bad[0][0] if bad else '',bad[-1][0] if bad else '')
  for i,l in bad[:2]:print(' ',i,l[:200])