import os,re
d='/task/fixtures/round-05/'
for i,l in enumerate(open(d+'board.md'),1):print('board',i,l.rstrip())
for f in sorted(os.listdir(d+'logs')):
  L=open(d+'logs/'+f).read().splitlines()
  e=[i for i,l in enumerate(L,1) if re.search('ERROR|WARN|heap',l) and 'slow query' not in l]
  print(f,len(e),e[:15]);
  if e:print(' ',L[e[0]-1][:150])
  if L:print(' first:',L[0][:150])