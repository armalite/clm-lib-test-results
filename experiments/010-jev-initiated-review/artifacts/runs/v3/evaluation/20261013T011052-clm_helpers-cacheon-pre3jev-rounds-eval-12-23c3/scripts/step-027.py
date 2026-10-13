import os,re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  e=[(i,l) for i,l in enumerate(L,1) if re.search(r'ERR|error|429|expired|fail',l,re.I)]
  print(f,len(e))
  for i,l in e[:3]:print(' ',i,l[:150])