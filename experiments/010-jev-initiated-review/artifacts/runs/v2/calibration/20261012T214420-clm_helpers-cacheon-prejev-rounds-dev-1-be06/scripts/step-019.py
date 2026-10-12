import re,glob
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
    n=f.split('/')[-1]
    hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if 'slow query' not in l and not re.search(r'INFO|level=info',l)]
    print('==',n,len(hits))
    for i,l in hits[:6]: print(i,l[:150])
    if len(hits)>6: print('... last',hits[-1][0])
