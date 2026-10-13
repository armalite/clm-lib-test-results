import glob
print(open('/task/fixtures/round-02/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if 'slow query' not in l and ('ERROR' in l or 'WARN' in l or 'error' in l):
            print(f.split('/')[-1],i,l.strip()[:160])