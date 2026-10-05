import re,glob
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
skip=re.compile(r'request ok|heartbeat|gc |health ok|slow query|heap',re.I)
for f in sorted(glob.glob(b+'logs/*.log')):
  n=f.split('/')[-1]
  for i,l in enumerate(open(f),1):
    if not skip.search(l) and re.search(r'WARN|ERR|FATAL|fail|error',l,re.I):print(n,i,l.rstrip()[:150])