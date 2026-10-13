import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    hits=[]
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|429|cert|lag|backlog|ttl|stampede|oom|disk|dns',l,re.I) and 'slow' not in l.lower():
            hits.append((i,l.strip()[:150]))
    print(f.split('/')[-1],len(hits))
    for h in hits[:4]: print(' ',h)