import re,glob
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if not re.search(r'slow.query|INFO',l)]
  print(f.split('/')[-1],len(L))
  for i,l in L[:3]+L[-2:]:print(' ',i,l[:150])