import glob
for f in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-04/'+f),1): print(f,i,l.rstrip()[:200])
for p in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    n=0
    for i,l in enumerate(open(p),1):
        if ('ERROR' in l or 'FATAL' in l) and n<8:
            n+=1; print(p.split('/')[-1],i,l.strip()[:120])