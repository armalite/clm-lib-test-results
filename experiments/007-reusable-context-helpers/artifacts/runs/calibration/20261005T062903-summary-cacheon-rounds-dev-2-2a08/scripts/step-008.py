import glob
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.strip()[:300])
for f in sorted(glob.glob(b+'logs/*.log')):
    n=0
    for i,l in enumerate(open(f),1):
        if ('ERROR' in l or 'WARN' in l or 'error' in l.lower() or 'level=e' in l.lower()) and 'slow' not in l:
            n+=1
            if n<=6: print(f.split('/')[-1],i,l.strip()[:140])
    print(f.split('/')[-1],'count',n)
    print('first',open(f).readline().strip()[:140])
