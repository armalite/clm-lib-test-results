import re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.strip()[:200])
import os
for s in sorted(os.listdir(b+'logs')):
    L=open(b+'logs/'+s).read().splitlines()
    hits=[(i,l) for i,l in enumerate(L,1) if re.search(r'error|warn|lag|cert|429|pool|oom|memory|disk|dns|ttl|miss',l,re.I)]
    print(s,len(hits))
    for i,l in hits[:4]+hits[-2:]: print(' ',i,l[:160])