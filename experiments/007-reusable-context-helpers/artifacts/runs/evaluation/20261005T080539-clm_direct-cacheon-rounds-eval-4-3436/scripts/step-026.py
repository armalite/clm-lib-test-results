import re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
    n=0
    for i,l in enumerate(open(b+'logs/'+f),1):
        if re.search(r'WARN|ERROR|429|pool|ttl|leak|memory',l,re.I) and 'slow query' not in l:
            n+=1
            if n<=4:print(f,i,l.rstrip()[:150])
    print(f,'hits',n)