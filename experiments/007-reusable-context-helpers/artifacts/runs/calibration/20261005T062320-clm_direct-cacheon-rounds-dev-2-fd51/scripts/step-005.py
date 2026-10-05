import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1): print(f,i,l.rstrip()[:200])
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|error|fail',l) and 'slow query' not in l:
      n+=1
      if n<=6: print(f.split('/')[-1],i,l.strip()[:150])
  print(f.split('/')[-1],'count',n)