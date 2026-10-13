import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if not re.search('slow query|request ok|gc|health|heartbeat',l)]
  print(f.split('/')[-1],len(h))
  for x in h[:5]:print(x)