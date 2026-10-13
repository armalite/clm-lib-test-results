import glob
for f in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    n=p.split('/')[-1];hits=[]
    for i,l in enumerate(open(p),1):
        if 'INFO' in l or 'slow query' in l:continue
        hits.append((i,l.strip()[:110]))
    print(n,len(hits))
    for h in hits[:4]:print(' ',h)
    print('  lines',[h[0] for h in hits][:30])