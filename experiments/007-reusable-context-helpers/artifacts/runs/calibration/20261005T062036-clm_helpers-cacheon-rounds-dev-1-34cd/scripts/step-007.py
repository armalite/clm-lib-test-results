import os,re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l)
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if not re.search(r'\bINFO\b|level=info|"info"',l,re.I)]
  print(f,len(hits))
  for i,l in hits[:6]:print(' ',i,l[:150])