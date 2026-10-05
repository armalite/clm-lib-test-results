import re,glob
print(open('/task/fixtures/round-11/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
    L=[(i+1,l) for i,l in enumerate(open(f)) if not re.search('slow query|INFO|/v1/health',l)]
    print(f.split('/')[-1],len(L),L[0][0] if L else '',L[-1][0] if L else '')
    for i,l in L[:2]: print(i,l.strip()[:150])