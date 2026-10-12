import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*')):
  L=[str(i) for i,l in enumerate(open(f),1) if ('slow query' not in l and re.search('ERROR|WARN|429|exhaust|valid',l))]
  print(f.split('/')[-1],','.join(L))
  for i,l in enumerate(open(f),1):
    if str(i) in L[:1]:print(l.rstrip()[:200])