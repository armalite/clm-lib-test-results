import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    L=open(f).read().splitlines();e=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERR|error|429|expired|fail',l,re.I)]
    print(f.split('/')[-1],len(e))
    for i,l in e[:3]:print(' ',i,l[:150])