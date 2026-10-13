import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+f),1) if re.search('ERROR|429|FAIL|error',l) and 'slow query' not in l]
  print(f,len(L))
  for x in L[:2]+L[-1:]:print(' ',x[0],x[1][:150])