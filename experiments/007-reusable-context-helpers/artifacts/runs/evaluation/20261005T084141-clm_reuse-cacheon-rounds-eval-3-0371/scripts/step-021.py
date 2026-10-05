import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l[:150]) for i,l in enumerate(L) if re.search(r'ERROR|429|heap|disk|cert|OOM|restart',l,re.I)]
    print(f.split('/')[-1],len(hits))
    for h in hits[:4]+hits[-2:]: print(h)