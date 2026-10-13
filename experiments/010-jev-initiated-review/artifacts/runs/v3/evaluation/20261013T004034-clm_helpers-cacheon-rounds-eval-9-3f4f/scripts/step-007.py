import re,glob
print(open('/task/fixtures/round-03/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    L=open(f).read().splitlines()
    bad=[(i+1,l) for i,l in enumerate(L) if not re.search('heartbeat|health ok|request ok|gc cycle|slow query',l)]
    print(f.split('/')[-1],len(bad))
    for i,l in bad[:4]+bad[-2:]: print(i,l[:150])