import re,glob
print(open('/task/fixtures/round-05/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|error|429|disk|heap|cert|WARN',l) and 'slow query' not in l]
    print(f.split('/')[-1],len(hits))
    for i,l in hits[:4]+hits[-2:]: print(i,l[:160])