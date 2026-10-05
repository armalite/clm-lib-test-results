import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1): print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-07/logs/*')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(p),1) if 'INFO' not in l and 'slow' not in l.lower()]
  print(p.split('/')[-1],len(ls))
  for i,l in ls[:3]+ls[-2:]: print(i,l[:160])