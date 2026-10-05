import re,glob
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|error|fail|expired|ttl',l):hits.append(i)
  print(f.split('/')[-1],hits)
  if hits:print(open(f).read().splitlines()[hits[0]-1][:200])