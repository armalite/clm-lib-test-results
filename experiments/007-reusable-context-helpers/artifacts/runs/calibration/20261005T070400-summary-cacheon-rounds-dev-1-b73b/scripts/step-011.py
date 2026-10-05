import os,re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip(): print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  c={}
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ' INFO ' in l or 'INFO' in l[:40] and 'level' not in l: continue
    k=re.sub(r'\d+','N',l[20:])[:70]
    c.setdefault(k,[]).append(i)
  for k,v in c.items(): print(f,v[:6],len(v),k.strip())