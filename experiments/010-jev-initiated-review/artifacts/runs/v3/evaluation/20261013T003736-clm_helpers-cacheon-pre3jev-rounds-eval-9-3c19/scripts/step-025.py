import re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
import os
for f in sorted(os.listdir(b+'logs')):
    for i,l in enumerate(open(b+'logs/'+f),1):
        if re.search(r'ERROR|FATAL|429|cert|SERVFAIL|pool|oom|restart|lag|disk|invalid',l,re.I) and 'slow query' not in l:print(f,i,l.rstrip()[:150])