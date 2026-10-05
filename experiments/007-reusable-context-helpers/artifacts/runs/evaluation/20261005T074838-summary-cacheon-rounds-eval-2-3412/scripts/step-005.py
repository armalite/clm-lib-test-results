import glob,re
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if 'slow query' in l or ' INFO ' in l or 'heap usage' in l or 'gc cycle' in l: continue
        print(f.split('/')[-1],i,l.strip()[:150])
