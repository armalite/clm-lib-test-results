import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    L=[(i+1,l.strip()) for i,l in enumerate(open(f)) if not re.search(r'slow query|request ok|heartbeat|gc |health ok',l)]
    print(f.split('/')[-1],len(L))
    if L: print(L[0],L[-1]);
    for i,l in L[:3]: print(i,l[:160])