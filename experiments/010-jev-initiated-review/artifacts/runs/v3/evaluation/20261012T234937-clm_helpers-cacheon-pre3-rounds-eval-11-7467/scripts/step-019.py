import os,re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+f),1) if re.search('ERROR|FATAL|error',l)]
  print(f,len(L))
  for x in L[:2]+L[-1:]:print(' ',x[0],x[1][:160])