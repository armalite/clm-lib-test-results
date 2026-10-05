import glob
print(open('/task/fixtures/round-05/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  s=f.split('/')[-1][:-4]
  for i,l in enumerate(open(f),1):
    if ' INFO ' not in l and 'slow query' not in l: print(s,i,l.strip()[11:110])