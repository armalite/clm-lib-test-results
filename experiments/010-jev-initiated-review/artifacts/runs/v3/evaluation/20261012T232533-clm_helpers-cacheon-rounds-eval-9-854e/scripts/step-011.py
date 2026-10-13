import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*')):
  n=f.split('/')[-1]
  hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|FATAL|CRIT|429|OOM|lag|disk|cert|config|inflight',l,re.I) and not re.search('slow',l,re.I)]
  print(n,len(hits))
  for i,l in hits[:4]+hits[-2:]: print(' ',i,l[:170])