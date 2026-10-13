import re
for f in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
    for i,l in enumerate(open(p),1):
        if re.search('ERROR|WARN|FATAL|error|warn',l) and 'slow query' not in l:print(p.split('/')[-1],i,l.rstrip()[:150])