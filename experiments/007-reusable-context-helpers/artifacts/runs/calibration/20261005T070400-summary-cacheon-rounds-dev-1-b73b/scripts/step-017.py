import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  h=[(i,l.strip()[:110]) for i,l in enumerate(open(f),1) if not re.search(r'slow query|heartbeat|health ok|gc cycle|request ok',l)]
  print(f.split('/')[-1],len(h))
  for x in h[:6]:print(x)