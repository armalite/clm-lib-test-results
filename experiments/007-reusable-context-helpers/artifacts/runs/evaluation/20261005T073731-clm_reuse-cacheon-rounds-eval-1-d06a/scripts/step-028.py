import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
import os
for s in os.listdir(b+'logs'):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+s),1) if not re.search(r'INFO|slow',l)]
  print(s,len(ls),[x[0] for x in ls][:40]); print(ls[:2])