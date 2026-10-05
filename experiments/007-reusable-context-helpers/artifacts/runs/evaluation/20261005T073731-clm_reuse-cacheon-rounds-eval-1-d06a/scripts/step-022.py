import re,glob
for f in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
    n=p.split('/')[-1];hits=[]
    for i,l in enumerate(open(p),1):
        if 'INFO' in l or 'slow' in l: continue
        hits.append((i,l.strip()[:110]))
    print(n,len(hits))
    for h in hits[:4]+hits[-2:]:print(' ',h)