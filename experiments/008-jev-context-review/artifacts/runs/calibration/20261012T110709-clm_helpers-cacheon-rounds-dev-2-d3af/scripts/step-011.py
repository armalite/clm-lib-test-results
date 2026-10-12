import re,glob
print(open('/task/fixtures/round-04/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    L=open(f).read().splitlines()
    e=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|FATAL|error',l) and 'slow query' not in l]
    print(f.split('/')[-1],len(L),len(e))
    for i,l in e[:3]+e[-1:]: print(i,l[:170])