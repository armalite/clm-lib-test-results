import os,re
b='/task/fixtures/round-06/'
for f in['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search(r'ERROR|FATAL|CRIT|error|fail',l) and not re.search(r'slow query|heartbeat|gc',l)]
  print(f,len(hits),[h[0] for h in hits][:40])
  for i,l in hits[:2]:print(' ',i,l[:200])
  if not hits:print(' first:',L[0][:200])