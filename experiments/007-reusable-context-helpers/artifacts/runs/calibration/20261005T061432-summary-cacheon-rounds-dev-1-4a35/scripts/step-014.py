import os,re
from collections import defaultdict
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip() and not l.startswith('#'): print(f,i,l.rstrip())
noise=re.compile(r'slow query|gc cycle|request ok|heartbeat|health ok')
for f in sorted(os.listdir(b+'logs')):
  d=defaultdict(list)
  for i,l in enumerate(open(b+'logs/'+f),1):
    if noise.search(l): continue
    p=l.split(' ',3)
    k=re.sub(r'\d+','N',p[-1])[:70]
    d[k].append(i)
  for k,v in d.items(): print(f,v[0],v[-1],len(v),k.strip())