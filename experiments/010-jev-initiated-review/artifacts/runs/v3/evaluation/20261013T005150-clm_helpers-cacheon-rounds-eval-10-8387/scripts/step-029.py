import re,os
b='/task/fixtures/round-10/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERR|error|fail|429',l,re.I)]
  print(f,len(e),[x[0] for x in e][:3],[x[0] for x in e][-1:] , e[0][1][:150] if e else '')
n=open('/task/workspace/notes.md').read()
import json
open('/task/workspace/notes.md','w').write(n)
