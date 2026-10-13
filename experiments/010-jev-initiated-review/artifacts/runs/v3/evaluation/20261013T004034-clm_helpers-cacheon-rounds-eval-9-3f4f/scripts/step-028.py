import re,glob
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
r=re.compile('heartbeat|health ok|request ok|gc cycle|slow query',re.I)
for f in sorted(glob.glob(b+'logs/*')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if not r.search(l)]
  print(f.split('/')[-1],len(ls))
  for i,l in ls[:2]+ls[-1:]:print(' ',i,l[:150])