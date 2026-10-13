import re,glob
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|WARN|error|warn',l) and 'slow' not in l]
  if L:print(f.split('/')[-1],len(L),L[0],L[-1])