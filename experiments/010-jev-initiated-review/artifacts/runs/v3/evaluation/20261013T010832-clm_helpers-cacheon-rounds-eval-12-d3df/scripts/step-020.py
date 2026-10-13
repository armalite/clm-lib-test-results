import re,glob
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if not re.search('slow query|request ok|heartbeat|gc |health ok',l)]
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]+hits[-2:]:print(' ',h[0],h[1][:150])