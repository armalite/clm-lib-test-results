import re
print(open('/task/fixtures/round-09/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|WARN|FATAL',l) and 'slow query' not in l:
            print(f.split('/')[-1],i,l.strip()[:150])