import re,glob
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
noise=re.compile('heartbeat|health ok|gc cycle|slow query|request ok')
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i,l.strip()) for i,l in enumerate(open(f),1) if not noise.search(l)]
  print(f.split('/')[-1],len(L),L[0][0] if L else '',L[-1][0] if L else '')
  for i,l in L[:2]:print(' ',i,l[:150])