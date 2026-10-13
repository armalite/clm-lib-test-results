import re,os
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  bad=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|FATAL|SERVFAIL|429|refused|timeout',l,re.I)]
  print(f,len(bad))
  for i,l in bad[:2]+bad[-1:]:print(' ',i,l[:160])