import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  L=[(i+1,l.strip()) for i,l in enumerate(open(b+'logs/'+f)) if 'slow query' not in l and 'INFO' not in l]
  print(f,len(L))
  for x in L[:3]+L[-1:]:print(x[0],x[1][:150])