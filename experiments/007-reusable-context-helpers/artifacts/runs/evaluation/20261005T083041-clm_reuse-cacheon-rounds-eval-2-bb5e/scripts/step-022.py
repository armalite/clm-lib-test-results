import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['auth','inventory','ledger','payments','pricing']:
  L=open(b+'logs/'+s+'-svc.log').read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search(r'ERROR|SERVFAIL|cert|heap|429|disk|pool|lag|restart|OOM',l,re.I) and 'slow query' not in l]
  print(s,len(hits),[h[0] for h in hits][:3],[h[0] for h in hits][-1:] if hits else '')
  for h in hits[:2]:print('  ',h[1][:200])