import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  n=0
  for i,l in enumerate(open(p),1):
    if 'slow query' not in l and re.search(r'ERROR|WARN|error|fail|429|SERVFAIL',l,re.I):
      n+=1
      if n<=6:print(p.split('/')[-1],i,l.strip()[:130])
  print(p.split('/')[-1],'count',n)