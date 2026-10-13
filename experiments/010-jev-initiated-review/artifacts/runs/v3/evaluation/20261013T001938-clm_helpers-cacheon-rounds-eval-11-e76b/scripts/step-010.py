import re,glob
r='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(r+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(r+'logs/*')):
  hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|lag|OOM|disk|batch',l)]
  print(f.split('/')[-1],len(hits),hits[:1],hits[-1:] if hits else '')