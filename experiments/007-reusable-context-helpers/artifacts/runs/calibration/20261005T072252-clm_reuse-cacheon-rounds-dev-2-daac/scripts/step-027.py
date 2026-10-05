import os,re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+f),1) if re.search('ERROR|error|429|SERVFAIL|expired|invalid',l)]
  print(f,len(L),L[0][0] if L else '',L[-1][0] if L else '')
  for i,l in L[:2]:print(' ',i,l[:200])