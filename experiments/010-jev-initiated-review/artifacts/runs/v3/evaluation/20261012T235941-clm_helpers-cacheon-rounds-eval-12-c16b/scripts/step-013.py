import re,glob
print(open('/task/fixtures/round-05/board.md').read())
N=re.compile(r'heartbeat|health ok|gc cycle|slow query|request ok')
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    L=[(i+1,l.strip()) for i,l in enumerate(open(f)) if not N.search(l)]
    print(f.split('/')[-1],len(L))
    for i,l in L[:3]+L[-1:]: print(' ',i,l[:150])