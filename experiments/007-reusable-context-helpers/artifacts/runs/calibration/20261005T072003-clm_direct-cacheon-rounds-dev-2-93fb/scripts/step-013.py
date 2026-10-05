import re,glob
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1];hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ok|gc|health|heartbeat|slow query',l) and not re.search(r'ERROR|FATAL|SERVFAIL|cert|429|OOM|pool|lag|disk|evict',l,re.I):continue
    hits.append((i,l.rstrip()))
  print(n,len(hits),[h[0] for h in hits])
  for h in hits[:2]:print(' ',h[1][:160])