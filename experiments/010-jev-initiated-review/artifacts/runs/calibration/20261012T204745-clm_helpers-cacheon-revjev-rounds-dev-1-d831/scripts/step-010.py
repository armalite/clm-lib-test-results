import re,glob
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i,l.strip()) for i,l in enumerate(open(f),1) if re.search('WARN|ERROR|error|fail|429|exhaust',l,re.I)]
  print(f.split('/')[-1],len(L))
  for i,l in L[:4]:print(' ',i,l[:150])