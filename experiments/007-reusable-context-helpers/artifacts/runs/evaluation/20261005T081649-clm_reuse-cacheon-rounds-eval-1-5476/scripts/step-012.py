import glob,re
for f in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-04/'+f),1): print(f,i,l.rstrip()[:200])
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    n=0
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|FATAL|429|OOM|disk|cert|dns|pool|ttl|lag',l,re.I) and 'slow' not in l.lower():
            n+=1
            if n<=4: print(f.split('/')[-1],i,l.strip()[:160])
    print(f.split('/')[-1],'hits',n)