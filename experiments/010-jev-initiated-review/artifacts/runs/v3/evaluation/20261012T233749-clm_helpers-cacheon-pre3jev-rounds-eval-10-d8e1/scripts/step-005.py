import glob
print(open('/task/fixtures/round-02/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*')):
  for i,l in enumerate(open(f),1):
    if 'slow query' not in l and ('WARN' in l or 'ERROR' in l or 'error' in l):print(f.split('/')[-1],i,l[:140].strip())