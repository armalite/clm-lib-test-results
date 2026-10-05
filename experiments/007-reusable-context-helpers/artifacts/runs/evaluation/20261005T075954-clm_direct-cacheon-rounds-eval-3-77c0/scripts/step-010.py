import re,glob
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  n=f.split('/')[-1]
  hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search(r'ERROR|FATAL|CRIT|error=|status=5|429',l) and 'slow query' not in l]
  print(n,len(hits))
  for i,l in hits[:4]: print(' ',i,l[:200])
  if hits: print('  last',hits[-1][0])