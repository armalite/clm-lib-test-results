import os,re,collections
b='/task/fixtures/round-08/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
    L=open(b+'logs/'+f).read().splitlines()
    c=collections.defaultdict(list)
    for i,l in enumerate(L):
        if 'ERROR' in l:
            m=re.search(r'"msg":"([^"]*)"',l); c[m.group(1) if m else l[:60]].append(i+1)
    print(f,{k:(len(v),v[0],v[-1]) for k,v in c.items()})
