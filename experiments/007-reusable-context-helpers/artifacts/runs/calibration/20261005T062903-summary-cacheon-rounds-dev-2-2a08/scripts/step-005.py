import glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if ('ERROR' in l or 'WARN' in l or 'error' in l.lower()) and 'slow' not in l:
            print(f.split('/')[-1],i,l.strip()[:150])
