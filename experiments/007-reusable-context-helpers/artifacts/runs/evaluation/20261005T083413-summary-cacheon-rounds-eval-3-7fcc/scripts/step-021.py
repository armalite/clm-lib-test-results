import glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  s=f.split('/')[-1][:-4]
  n=0
  for i,l in enumerate(open(f),1):
    if 'INFO' not in l[:40] and 'slow query' not in l and 'level=info' not in l:
      n+=1
      if n<=5: print(s,i,l.strip()[:130])
  print(s,'count',n)