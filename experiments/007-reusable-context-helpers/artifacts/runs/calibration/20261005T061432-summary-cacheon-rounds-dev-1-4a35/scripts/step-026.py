import os,re
from collections import defaultdict
b='/task/fixtures/round-10/'
out=[]
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip() and not l.startswith('#'): out.append(f'{f} {i} {l.rstrip()}')
noise=re.compile(r'slow query|gc cycle|request ok|heartbeat|health ok')
for f in sorted(os.listdir(b+'logs')):
  d=defaultdict(list)
  for i,l in enumerate(open(b+'logs/'+f),1):
    if noise.search(l): continue
    k=re.sub(r'\d+','N',l[l.find('"msg"'):] if '"msg"' in l else l)[:90]
    d[k].append(i)
  for k,v in d.items(): out.append(f'{f} {v} {k.strip()}')
s='\n'.join(out);print(s)
open('/task/workspace/notes.md','a').write('\nR10 raw:\n'+s+'\n')