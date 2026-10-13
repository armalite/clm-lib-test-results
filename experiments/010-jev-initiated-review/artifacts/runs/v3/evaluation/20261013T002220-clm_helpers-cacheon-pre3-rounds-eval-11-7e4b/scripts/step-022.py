import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
import os
for s in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+s).read().splitlines()
  bad=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|WARN|error|fail',l) and 'slow query' not in l]
  print(s,len(bad))
  for i,l in bad[:3]+bad[-1:]:print(' ',i,l[:180])