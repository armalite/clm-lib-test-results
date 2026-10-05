import glob
print(open('/task/fixtures/round-06/board.md').read())
print(open('/task/fixtures/round-06/changes.md').read())
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  s=f.split('/')[-1][:-4]
  n=0
  for i,l in enumerate(open(f),1):
    if ' INFO ' not in l and 'slow query' not in l and 'INFO' not in l[:40]:
      n+=1
      if n<=6: print(s,i,l.strip()[11:120])
  print(s,'count',n)