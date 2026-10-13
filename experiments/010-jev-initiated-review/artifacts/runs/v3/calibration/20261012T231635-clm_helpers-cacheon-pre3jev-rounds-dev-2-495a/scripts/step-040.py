import os
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in os.listdir(b+'logs'):
  L=open(b+'logs/'+s).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l or 'error' in l.lower()]
  print(s,len(e),e[:2])