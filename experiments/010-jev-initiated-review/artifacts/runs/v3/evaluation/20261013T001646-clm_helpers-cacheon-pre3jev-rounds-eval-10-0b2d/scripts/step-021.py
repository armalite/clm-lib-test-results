import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  n=p.split('/')[-1]
  hits=[(i,l.rstrip()) for i,l in enumerate(open(p),1) if 'ERROR' in l or 'error' in l.lower() and 'slow' not in l]
  print(n,len(hits))
  for i,l in hits[:4]:print(' ',i,l[:150])