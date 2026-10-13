import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).readlines()
  hits=[(i+1,l.strip()) for i,l in enumerate(L) if re.search('ERROR|WARN|error|warn',l) and 'slow' not in l]
  print(f,len(hits))
  for h in hits[:2]+hits[-1:]: print(h)
