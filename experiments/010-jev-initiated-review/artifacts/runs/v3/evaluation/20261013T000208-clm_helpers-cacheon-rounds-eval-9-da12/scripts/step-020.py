import re,glob
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if not re.search('slow.query|INFO',l)]
  n=f.split('/')[-1]
  print(n,len(ls),'first',ls[:2],'last',ls[-1:] if ls else '')