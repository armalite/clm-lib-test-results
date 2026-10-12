import glob,re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  n=f.split('/')[-1]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|429|SERVFAIL|OOM|exhaust|invalid|lag|disk|cert',l,re.I) and not re.search('slow query|heartbeat|gc',l):print(n,i,l.rstrip()[:150])