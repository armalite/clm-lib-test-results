import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1): print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  c=0
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN|error|warn',l) and 'slow query' not in l:
      c+=1
      if c<=4: print(p.split('/')[-1],i,l.strip()[:160])
  print(p.split('/')[-1],'count',c)