import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    L=open(f).read().splitlines();hits=[i+1 for i,l in enumerate(L) if not re.search(r'INFO|slow query',l)]
    if hits:print(f.split('/')[-1],len(hits),hits[0],hits[-1],L[hits[0]-1][:160])