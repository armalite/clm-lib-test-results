import re
print(open('/task/fixtures/round-08/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l: print(f.split('/')[-1][:6],i,l.strip()[:110])