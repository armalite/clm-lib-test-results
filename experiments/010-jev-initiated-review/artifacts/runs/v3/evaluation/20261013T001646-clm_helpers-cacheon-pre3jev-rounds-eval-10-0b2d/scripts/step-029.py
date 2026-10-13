import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|429|SERVFAIL|OOM|disk|cert',l,re.I):
      n+=1
      if n<=4:print(f.split('/')[-1],i,l.rstrip()[:160])
  print(f.split('/')[-1],'count',n)