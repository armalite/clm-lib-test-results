import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
import glob
for f in sorted(glob.glob(b+'logs/*')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|SERVFAIL|429|FATAL|CRIT',l)]
  print(f.split('/')[-1],len(hits),hits[0][0] if hits else '',hits[-1][0] if hits else '')
  for i,l in hits[:2]:print(' ',i,l[:160])