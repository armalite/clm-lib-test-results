import os,re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+s).read().splitlines()
  e=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|FATAL|error|fail',l)]
  print(s,len(e))
  for i,l in e[:2]+e[-1:]:print(' ',i,l[:200])