import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    L=open(f).read().splitlines()
    bad=[(i+1,l) for i,l in enumerate(L) if not re.search('heartbeat|health ok|request ok|gc cycle|slow query',l)]
    print(f.split('/')[-1],len(bad),[b[0] for b in bad][:3],[b[0] for b in bad][-1:] if bad else '')
    for b in bad[:2]: print(' ',b[1][:160])