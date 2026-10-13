import re,os
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  hits=[(i,l.strip()[:150]) for i,l in enumerate(open(b+'logs/'+s),1) if re.search(r'ERROR|429|cert|config|lag|fail',l,re.I)]
  print(s,len(hits),[h[0] for h in hits][:15])
  for h in hits[:2]:print('  ',h)