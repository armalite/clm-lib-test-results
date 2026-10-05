import re
b='/task/fixtures/round-07/'
for f in['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l)
for s in['auth','inventory','ledger','payments','pricing']:
  L=open(b+'logs/%s-svc.log'%s).read().splitlines()
  h=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|SERVFAIL|heap|429|cert|pool|disk|lag|backoff|restart',l,re.I)]
  print(s,len(h),[i for i,_ in h][:3],[i for i,_ in h][-1:] if h else '')
  if h:print(' ',h[0][1][:200])