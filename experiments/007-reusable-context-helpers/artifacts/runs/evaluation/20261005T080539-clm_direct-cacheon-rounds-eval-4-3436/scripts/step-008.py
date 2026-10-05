import glob
print(open('/task/fixtures/round-03/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if 'INFO' not in l and 'slow query' not in l:
            print(f.split('/')[-1],i,l.strip()[:150])