import re,os,collections
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip():print(f,i,l.rstrip()[:200])
for f in sorted(os.listdir(b+'logs')):
  d=collections.defaultdict(list)
  for i,l in enumerate(open(b+'logs/'+f),1):
    k=re.sub(r'\d+','N',l.strip())[:80]
    if 'slow query' in k:continue
    d[k].append(i)
  for k,v in d.items():print(f,v[:6],len(v),k)
