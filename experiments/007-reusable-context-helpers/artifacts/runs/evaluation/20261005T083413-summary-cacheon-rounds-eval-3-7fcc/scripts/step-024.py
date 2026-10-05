import glob
print(open('/task/fixtures/round-08/board.md').read())
print(open('/task/fixtures/round-08/changes.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  s=f.split('/')[-1][:-4]
  n=0
  for i,l in enumerate(open(f),1):
    if 'INFO' not in l[:40] and 'slow query' not in l and 'level=info' not in l:
      n+=1
      if n<=4: print(s,i,l.strip()[:120])
  print(s,'count',n)