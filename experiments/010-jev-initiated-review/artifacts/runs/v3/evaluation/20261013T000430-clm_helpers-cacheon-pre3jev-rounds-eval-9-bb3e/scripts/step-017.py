import glob
print(open('/task/fixtures/round-05/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if 'INFO' not in l and 'slow query' not in l:
      n+=1
      if n<=4: print(f.split('/')[-1],i,l.strip()[:120])
  print(f.split('/')[-1],'count',n)