import re,os
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if re.search(r'SERVFAIL|429|ERROR|FATAL|OOM|disk|pool',l,re.I)]
  print(f,len(hits),hits[:3],hits[-1:] if hits else '')
  if hits: print(' ',L[hits[0]-1][:200])