import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  L=open(f).read().splitlines();hits=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|WARN|FATAL',l) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:3]+hits[-2:]:print(i,l[:150])