import re,os
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
kw=re.compile(r'error|fail|429|expire|pool|lag|mem|disk|dns|cert|inflight',re.I)
for f in sorted(os.listdir(b+'logs')):
    hits=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+f),1) if 'slow query' not in l and kw.search(l)]
    print(f,len(hits))
    for i,l in hits[:6]: print(' ',i,l[:150])