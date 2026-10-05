import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if 'INFO' not in l and 'slow query' not in l]
  print(f,len(hits))
  for h in hits[:4]+hits[-2:]: print(' ',h[0],h[1][:150])