import re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+f),1) if not re.search('slow query|INFO|/v1/health',l)]
  print(f,len(L))
  for x in L[:3]+L[-1:]: print(' ',x[0],x[1][:150])