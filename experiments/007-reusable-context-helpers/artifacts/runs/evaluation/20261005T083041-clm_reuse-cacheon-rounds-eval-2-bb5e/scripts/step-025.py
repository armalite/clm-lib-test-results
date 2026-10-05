import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    hits=[(i,l.strip()[:150]) for i,l in enumerate(open(f),1) if re.search(r'ERROR|SERVFAIL|certificate|heap|429|disk|lag|pool|restart',l,re.I)]
    print(f.split('/')[-1],len(hits),[h[0] for h in hits][:3],[h[0] for h in hits][-1:] if hits else '')
    if hits: print(' ',hits[0][1])