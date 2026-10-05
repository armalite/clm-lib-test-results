import glob,re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
    n=f.split('/')[-1]
    for i,l in enumerate(open(f),1):
        if 'slow query' in l: continue
        print(n,i,l.rstrip()[:150])