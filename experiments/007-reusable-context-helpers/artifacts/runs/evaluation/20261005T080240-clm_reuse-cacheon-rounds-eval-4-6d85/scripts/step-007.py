import glob,re
print(open('/task/fixtures/round-03/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'WARN|ERROR|FATAL',l) and 'slow query' not in l]
    print(f.split('/')[-1],len(hits))
    for i,l in hits[:3]+hits[-1:]: print(i,l[:160])
