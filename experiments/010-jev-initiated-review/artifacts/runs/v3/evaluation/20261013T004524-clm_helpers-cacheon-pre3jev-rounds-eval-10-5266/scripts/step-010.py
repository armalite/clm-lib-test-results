import glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and 'auth-svc' not in f: print(f.split('/')[-1],i,l.strip()[:150])
print(open('/task/fixtures/round-02/board.md').read()[:1500])
import os;print(os.path.exists('/task/fixtures/round-02/changes.md'))