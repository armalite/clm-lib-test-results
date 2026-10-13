import re,glob
d='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(d+f),1):print(f,i,l.rstrip()[:200])
for f in sorted(glob.glob(d+'logs/*')):
  hits=[(i,l) for i,l in enumerate(open(f),1) if re.search('ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|lag|OOM|disk|batch|SERVFAIL',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:2]+hits[-1:]:print(' ',i,l.rstrip()[:180])