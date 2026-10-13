import re,collections
b='/task/fixtures/round-06/'
for f in['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
N=re.compile('heartbeat|health ok|gc cycle|slow query|request ok')
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l.strip()) for i,l in enumerate(open(b+'logs/'+f),1) if not N.search(l)]
  if L:print(f,len(L),L[0][0],L[-1][0],L[0][1][:150])