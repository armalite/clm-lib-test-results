import os,re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+f),1) if 'slow query' not in l and 'INFO' not in l]
  print(f,len(L))
  for i,l in L[:3]+L[-1:]:print(' ',i,l[:160])