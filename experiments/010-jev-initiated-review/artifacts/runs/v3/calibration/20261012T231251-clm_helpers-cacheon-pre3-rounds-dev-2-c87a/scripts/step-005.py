import glob,re
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  n=0
  for i,l in enumerate(open(p),1):
    if 'slow query' not in l and re.search(r'ERROR|WARN|error|warn',l) and 'inventory' not in p:
      n+=1
      if n<=8:print(p.split('/')[-1],i,l.strip()[:120])
  print(p.split('/')[-1],'count',n)