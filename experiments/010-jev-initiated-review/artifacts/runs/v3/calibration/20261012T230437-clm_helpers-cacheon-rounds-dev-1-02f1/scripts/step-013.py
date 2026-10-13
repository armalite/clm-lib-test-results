import os,re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  hits=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+s),1) if not re.search(r'INFO|slow query',l)]
  print(s,len(hits))
  for i,l in hits[:6]:print(' ',i,l[:150])
  if hits:print('  lines',[i for i,_ in hits])