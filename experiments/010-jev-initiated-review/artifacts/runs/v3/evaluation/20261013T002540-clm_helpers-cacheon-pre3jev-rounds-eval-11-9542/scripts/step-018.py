import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-05/logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(p),1) if ('ERROR' in l or '429' in l or 'FATAL' in l or 'error' in l) and 'slow query' not in l]
  print(p.split('/')[-1],len(L))
  for i,l in L[:3]+L[-1:]:print(i,l[:160])