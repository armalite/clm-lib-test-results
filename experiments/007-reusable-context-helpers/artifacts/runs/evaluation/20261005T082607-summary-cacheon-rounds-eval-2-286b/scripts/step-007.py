import re,glob
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for p in sorted(glob.glob(b+'logs/*')):
  n=p.split('/')[-1]
  L=open(p).read().splitlines()
  print(n,'first:',L[0][:150])
  for i,l in enumerate(L,1):
    if 'slow query' in l: continue
    if re.search(r'ERROR|WARN|FATAL|429|cert|dns|pool|lag|disk|OOM|restart|config|heap',l,re.I): print(n,i,l[:140])