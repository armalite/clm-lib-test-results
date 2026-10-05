import re,glob
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1]
  for i,l in enumerate(open(f),1):
    if re.search(r'request ok|heartbeat|gc |health ok|slow query',l):continue
    print(n,i,l.rstrip()[:150])