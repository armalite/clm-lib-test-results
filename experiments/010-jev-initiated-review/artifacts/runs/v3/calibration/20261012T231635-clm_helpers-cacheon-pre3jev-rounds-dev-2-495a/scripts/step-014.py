import re,glob
print(open('/task/fixtures/round-04/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|WARN|error|fail|expired|429|pool|disk|memory|lag',l)]
    print(f.split('/')[-1],len(hits))
    for h in hits[:3]+hits[-1:]: print(' ',h[0],h[1][:150])