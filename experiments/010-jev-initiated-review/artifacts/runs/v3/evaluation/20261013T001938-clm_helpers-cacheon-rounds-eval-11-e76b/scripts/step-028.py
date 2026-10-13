import re,glob
d='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(d+f),1):print(f,i,l.rstrip()[:200])
for f in sorted(glob.glob(d+'logs/*')):
  hits=[(i,l) for i,l in enumerate(open(f),1) if re.search(r'ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|SERVFAIL|lag|OOM|disk|batch|heap',l,re.I)]
  print(f.split('/')[-1],len(hits),hits[0][0] if hits else '',hits[-1][0] if hits else '')
  for i,l in hits[:2]:print(' ',i,l.rstrip()[:180])