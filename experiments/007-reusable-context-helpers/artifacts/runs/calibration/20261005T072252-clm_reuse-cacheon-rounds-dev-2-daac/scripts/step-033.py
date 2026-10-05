import os
b='/task/fixtures/round-11/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l or 'error' in l.lower()]
  print(f,len(e),[x[0] for x in e][:20])
  for x in e[:2]: print(' ',x[0],x[1][:160])