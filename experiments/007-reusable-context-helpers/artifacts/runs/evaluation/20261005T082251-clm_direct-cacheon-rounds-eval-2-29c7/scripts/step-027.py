import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    n=f.split('/')[-1];c={}
    for i,l in enumerate(open(f),1):
        if re.search(r'request ok|heartbeat|gc |health ok|slow query|heap',l):continue
        k=re.sub(r'[0-9:T.\-]{8,}','',l)[:70]
        c.setdefault(k[:40],[]).append(i)
    for k,v in c.items():print(n,k,v[:3],len(v))
