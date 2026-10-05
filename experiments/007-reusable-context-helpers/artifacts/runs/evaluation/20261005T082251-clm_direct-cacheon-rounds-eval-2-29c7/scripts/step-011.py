import re,glob
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob(b+'logs/*')):
  n=p.split('/')[-1]
  for i,l in enumerate(open(p),1):
    if not re.search(r'request ok|heartbeat|gc |health ok|slow query|heap',l):print(n,i,l.rstrip()[:160])