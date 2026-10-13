import glob
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l)
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f).read().splitlines(),1):
    if 'slow query' not in l and ('ERROR' in l or 'WARN' in l):print(f[len(b):],i,l[:160])