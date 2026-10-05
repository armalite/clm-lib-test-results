import os
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
    ls=open(b+'logs/'+f).read().splitlines()
    hits=[(i,l) for i,l in enumerate(ls,1) if 'INFO' not in l and 'slow' not in l.lower()]
    print(f,len(hits))
    for i,l in hits[:4]+hits[-2:]: print(' ',i,l[:150])