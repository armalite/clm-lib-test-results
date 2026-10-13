import subprocess
print(open('/task/fixtures/round-04/board.md').read());print(open('/task/fixtures/round-04/changes.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or 'error' in l.lower() and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:150])