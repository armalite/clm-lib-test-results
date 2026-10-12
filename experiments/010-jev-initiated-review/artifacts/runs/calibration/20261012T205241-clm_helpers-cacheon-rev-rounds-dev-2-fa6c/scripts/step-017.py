import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|error|FATAL|fail',l)]
  print(f.split('/')[-1],len(L))
  for i,l in L[:3]+L[-1:]:print(' ',i,l[:200])