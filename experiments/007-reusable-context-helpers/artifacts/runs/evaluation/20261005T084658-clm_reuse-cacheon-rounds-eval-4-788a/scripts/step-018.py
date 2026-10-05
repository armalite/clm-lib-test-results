import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
    for i,l in enumerate(open(b+'logs/'+f),1):
        if re.search(r'ERROR|WARN|429|pool|memory|oom|restart|cache|dns|cert|disk|lag',l,re.I) and 'slow query' not in l:print(f,i,l.rstrip()[:150])