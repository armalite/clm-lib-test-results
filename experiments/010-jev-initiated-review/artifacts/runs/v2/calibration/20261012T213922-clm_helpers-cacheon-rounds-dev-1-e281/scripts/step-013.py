import os,re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  hits=[]
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'slow query' in l.lower() or 'INFO' in l: continue
    hits.append((i,l.strip()[:110]))
  print(f,len(hits))
  seen=set()
  for i,l in hits:
    k=re.sub(r'[0-9]','',l)[25:70]
    if k in seen: continue
    seen.add(k);print(' ',i,l)
  print('  lines',[i for i,_ in hits])