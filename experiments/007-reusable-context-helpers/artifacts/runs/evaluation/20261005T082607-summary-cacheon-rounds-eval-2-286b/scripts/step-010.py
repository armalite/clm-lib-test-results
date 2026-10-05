import os
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
    L=open(b+'logs/'+f).read().splitlines()
    print(f,'first:',L[0][:120])
    n=0
    for i,l in enumerate(L,1):
        if ('INFO' not in l and 'slow query' not in l) or 'error' in l.lower():
            if 'heap usage' in l:
                n+=1
                if n>2:continue
            print(f,i,l[:130])
    print(f,'heap count',n)