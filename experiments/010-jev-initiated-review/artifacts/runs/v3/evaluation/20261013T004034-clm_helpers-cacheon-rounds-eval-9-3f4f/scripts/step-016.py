import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
pat=re.compile(r'heartbeat|health ok|request ok|gc cycle|slow query',re.I)
for f in sorted(glob.glob(b+'logs/*.log')):
    ls=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if not pat.search(l)]
    n=f.split('/')[-1]
    print(n,len(ls),'first',ls[:2],'last',ls[-1:] if ls else '')
    kinds={}
    for i,l in ls:
        k=re.sub(r'\d+','#',l)[-60:]
        kinds.setdefault(k,[]).append(i)
    for k,v in list(kinds.items())[:4]:print('  ',v[0],v[-1],len(v),k)