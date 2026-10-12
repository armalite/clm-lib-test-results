import os,re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  hits=[]
  for i,l in enumerate(open(b+'logs/'+s),1):
    if re.search(r'ERROR|WARN|429|exhaust|cert|dns|memory|disk|lag|inflight',l,re.I) and 'slow' not in l.lower():hits.append((i,l.strip()[:110]))
  print(s,len(hits))
  for h in hits[:4]:print(' ',h)