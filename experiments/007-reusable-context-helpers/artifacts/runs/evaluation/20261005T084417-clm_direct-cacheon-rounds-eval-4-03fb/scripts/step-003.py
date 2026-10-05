import os,glob
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  L=open(f).read().splitlines()
  e=[(i,l[:120]) for i,l in enumerate(L,1) if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l]
  print(os.path.basename(f),len(L),len(e))
  for x in e[:4]:print(' ',*x)