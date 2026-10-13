import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*')):
  for i,l in enumerate(open(f),1):
    if 'slow query' in l: continue
    if re.search(r'error|fail|429|expire|pool|lag|mem|disk|dns|cert|inflight|stampede|miss',l,re.I): print(f.split('/')[-1],i,l.strip()[:150])