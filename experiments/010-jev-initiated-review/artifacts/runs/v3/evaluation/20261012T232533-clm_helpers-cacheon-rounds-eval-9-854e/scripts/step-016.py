import re,glob
print(open('/task/fixtures/round-05/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    n=f.split('/')[-1];hits=[]
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|FATAL|pool|429|OOM|disk|cert|SERVFAIL|lag',l,re.I) and 'slow' not in l.lower(): hits.append((i,l.strip()[:150]))
    print(n,len(hits))
    for h in hits[:3]+hits[-2:]: print(' ',h)