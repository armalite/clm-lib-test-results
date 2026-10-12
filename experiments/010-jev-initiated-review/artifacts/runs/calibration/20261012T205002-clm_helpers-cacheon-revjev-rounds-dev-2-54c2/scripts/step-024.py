import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|error|429|certificate|SERVFAIL|max_inflight',l) and not re.search(r'slow|heartbeat|gc',l)]
    print(f.split('/')[-1],len(hits),[h[0] for h in hits])
    for h in hits[:2]: print(' ',h[0],h[1][:200])