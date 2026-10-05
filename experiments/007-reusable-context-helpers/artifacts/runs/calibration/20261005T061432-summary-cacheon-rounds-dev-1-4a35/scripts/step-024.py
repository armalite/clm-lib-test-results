import os,re
from collections import defaultdict
b='/task/fixtures/round-09/'
out=[]
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip() and not l.startswith('#'): out.append(f'{f} {i} {l.rstrip()}')
noise=re.compile(r'slow query|gc cycle|request ok|heartbeat|health ok')
for f in sorted(os.listdir(b+'logs')):
  d=defaultdict(list)
  for i,l in enumerate(open(b+'logs/'+f),1):
    if noise.search(l): continue
    k=re.sub(r'\d+','N',l.split(' ',3)[-1])[:70]
    d[k].append(i)
  for k,v in d.items(): out.append(f'{f} {v[0]}-{v[-1]} {len(v)} {k.strip()}')
s='\n'.join(out);print(s)
open('/task/workspace/notes.md','a').write('\nR9 raw:\n'+s+'\n')