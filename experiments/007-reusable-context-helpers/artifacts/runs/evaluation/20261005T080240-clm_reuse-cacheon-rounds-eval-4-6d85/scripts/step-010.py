import re,glob
print(open('/task/fixtures/round-04/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    ls=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(ls) if re.search(r'WARN|ERROR|error|warn',l) and 'slow query' not in l]
    print(f.split('/')[-1],len(hits))
    if hits: print(hits[0]); print(hits[-1])
