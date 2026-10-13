import os,re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+s),1) if re.search(r'ERROR|WARN|error|fail|429|denied|invalid',l,re.I)]
  print(s,len(L))
  for i,l in L[:4]:print(' ',i,l[:160])
  if L:print('  lines',[i for i,_ in L])