import glob
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f),1):
    if '"INFO"' not in l and 'slow query' not in l:print(f.split('/')[-1],i,l.rstrip()[:150])