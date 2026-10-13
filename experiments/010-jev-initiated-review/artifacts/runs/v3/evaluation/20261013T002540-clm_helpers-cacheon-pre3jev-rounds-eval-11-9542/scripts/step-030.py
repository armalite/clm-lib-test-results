import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
    for i,l in enumerate(open(b+'logs/'+f),1):
        if 'slow query' in l:continue
        if re.search(r'ERROR|429|restart|mem|OOM|batch|FATAL',l,re.I):print(f,i,l.rstrip()[:150])