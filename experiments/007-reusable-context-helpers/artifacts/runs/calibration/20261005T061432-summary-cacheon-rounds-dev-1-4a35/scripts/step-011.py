import os,re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip(): print(f,i,l.rstrip())
noise=re.compile(r'slow query|gc cycle|request ok|heartbeat|health ok')
from collections import defaultdict
for f in sorted(os.listdir(b+'logs')):
  d=defaultdict(list)
  for i,l in enumerate(open(b+'logs/'+f),1):
    if noise.search(l): continue
    k=re.sub(r'\d+','N',l.split(' ',3)[-1] if len(l.split())>3 else l)[:70]
    d[k].append(i)
  for k,v in d.items(): print(f,v[:6],len(v),k.strip())