import re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip()[:200])
import os
for f in sorted(os.listdir(b+'logs')):
    c={}
    for i,l in enumerate(open(b+'logs/'+f),1):
        if re.search(r'ERROR|WARN|429|pool|miss|mem|disk|dns|cert|lag',l,re.I) and not re.search('slow query',l,re.I):
            k=re.sub(r'[0-9]+','#',l)[30:90]
            c.setdefault(k,[]).append(i)
    for k,v in c.items(): print(f,v[:8],len(v),k)