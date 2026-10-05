import glob
for n in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-03/'+n),1): print(n,i,l.rstrip()[:300])
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if any(k in l for k in ['slow query',' INFO ','heap usage','gc cycle','request ok','health ok','heartbeat']): continue
        print(f.split('/')[-1],i,l.strip()[:140])
