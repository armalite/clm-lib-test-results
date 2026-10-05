import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(p),1) if re.search('ERROR|FATAL|error|429|cert|DNS|OOM|disk',l) and 'slow query' not in l]
  print(p.split('/')[-1],len(ls))
  for i,l in ls[:4]:print(' ',i,l[:200])