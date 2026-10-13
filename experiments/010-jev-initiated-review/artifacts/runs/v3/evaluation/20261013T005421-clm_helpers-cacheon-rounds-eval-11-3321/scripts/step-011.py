import glob
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if 'slow query' not in l and 'INFO' not in l]
  print(f.split('/')[-1],len(ls))
  for i,l in ls[:3]+ls[-1:]:print(i,l[:160])