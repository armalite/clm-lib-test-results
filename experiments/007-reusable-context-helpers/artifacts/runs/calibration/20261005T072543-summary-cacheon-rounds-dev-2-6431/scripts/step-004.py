import glob
R='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(R+f).read().splitlines(),1): print(f,i,l)
for p in sorted(glob.glob(R+'logs/*.log')):
  for i,l in enumerate(open(p).read().splitlines(),1):
    if 'slow query' not in l and ('ERROR' in l or 'WARN' in l): print(p.split('/')[-1],i,l[:130])