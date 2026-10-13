import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error|warn',l) and 'slow query' not in l]
  print(f,len(e),e[:2],e[-1:] if e else '')