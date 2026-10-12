import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|CRIT|SERVFAIL|429|refused|exhaust|OOM|expired|lag|disk|invalid',l,re.I) and 'slow query' not in l.lower():print(f.split('/')[-1],i,l.rstrip()[:150])