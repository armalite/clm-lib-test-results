import glob,re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for p in sorted(glob.glob(b+'logs/*.log')):
    for i,l in enumerate(open(p),1):
        if ('INFO' in l and 'ok' in l) or 'heartbeat' in l or 'slow query' in l: continue
        print(p.split('/')[-1],i,l.rstrip()[:160])