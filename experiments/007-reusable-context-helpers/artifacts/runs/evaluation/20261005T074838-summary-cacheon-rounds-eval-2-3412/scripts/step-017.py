import os,re
d='/task/fixtures/round-06/'
for fn in ['board.md','changes.md']:
  for i,l in enumerate(open(d+fn),1):print(fn,i,l.rstrip()[:200])
for f in sorted(os.listdir(d+'logs')):
  L=open(d+'logs/'+f).read().splitlines()
  e=[i for i,l in enumerate(L,1) if re.search('ERROR|WARN|heap|err',l,re.I) and 'slow query' not in l]
  print(f,len(e),e[:15])
  if e:print(' ',L[e[0]-1][:150])
  print(' first:',L[0][:120])