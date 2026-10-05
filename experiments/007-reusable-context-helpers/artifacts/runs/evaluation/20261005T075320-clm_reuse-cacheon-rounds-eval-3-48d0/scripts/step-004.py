import ctx,os
ctx.keep_only(['n1'])
b='/task/fixtures/round-02/'
for f in('board.md','changes.md'):
    for i,l in enumerate(open(b+f),1):print(f,i,l.strip()[:200])
r=b+'logs/'
for f in sorted(os.listdir(r)):
    n=0
    for i,l in enumerate(open(r+f),1):
        if 'slow query' not in l and any(k in l for k in('ERROR','WARN','429','fail','error')):
            n+=1
            if n<=4:print(f,i,l[:150].strip())
    print(f,'count',n)