import glob,os
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob(b+'logs/*.log')):
    c={}
    for i,l in enumerate(open(p),1):
        if 'ERROR' in l or 'WARN' in l:
            k=l[60:130];c.setdefault(k,[]).append(i)
    for k,v in c.items():print(os.path.basename(p)[:6],v[:4],len(v),k)