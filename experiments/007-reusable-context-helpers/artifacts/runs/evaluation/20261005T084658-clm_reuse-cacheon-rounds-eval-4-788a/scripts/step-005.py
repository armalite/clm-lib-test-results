import os,glob
print(open('/task/fixtures/round-02/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l: print(os.path.basename(f),i,l.strip()[:140])