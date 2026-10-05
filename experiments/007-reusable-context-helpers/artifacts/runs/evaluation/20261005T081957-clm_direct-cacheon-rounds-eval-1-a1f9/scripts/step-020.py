import os,re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|lag|WARN',l) and 'slow query' not in l]
  print(f,len(hits))
  for i,l in hits[:4]:print(' ',i,l[:200])