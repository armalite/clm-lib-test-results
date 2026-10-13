import glob
for f in sorted(glob.glob('/task/fixtures/round-02/*.md')):
    print(f);print(open(f).read())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:160])