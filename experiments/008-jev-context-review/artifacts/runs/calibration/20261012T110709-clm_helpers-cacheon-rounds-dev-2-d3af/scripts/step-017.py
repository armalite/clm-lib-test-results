import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=open(f).read().splitlines();e=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|FATAL|CRIT',l)]
  print(f.split('/')[-1],len(e))
  for i,l in e[:2]+e[-1:]:print(' ',i,l[:150])
