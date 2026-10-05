import os,re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip(): print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+s).read().splitlines()
  hits=[i for i,l in enumerate(L,1) if re.search('certificate_expired|config validation|lag|ERROR',l)]
  print(s,len(hits),hits[:8])
  if hits: print('  ',L[hits[0]-1][:200])
