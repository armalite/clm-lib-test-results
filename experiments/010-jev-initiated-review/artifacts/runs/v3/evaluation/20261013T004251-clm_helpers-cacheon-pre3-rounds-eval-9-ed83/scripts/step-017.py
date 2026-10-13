import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|429|fail|FAIL|expired|OOM|lag|pool|inflight|disk',l,re.I) and 'slow query' not in l]
  print(f,len(hits))
  for h in hits[:3]: print(h[0],h[1][:160])
  if hits: print('lines',[h[0] for h in hits])