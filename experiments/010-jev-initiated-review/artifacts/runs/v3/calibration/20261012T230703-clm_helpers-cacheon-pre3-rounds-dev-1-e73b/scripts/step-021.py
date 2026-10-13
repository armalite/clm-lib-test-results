import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|429|exhaust|miss|inflight|cert|dns|lag|memory|disk',l,re.I)]
  print(f,len(hits),hits[:2],hits[-1:] if hits else '')