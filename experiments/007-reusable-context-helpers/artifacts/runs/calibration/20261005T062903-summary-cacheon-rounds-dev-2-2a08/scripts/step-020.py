import os,re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
    L=open(b+'logs/'+f).read().splitlines()
    e=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|WARN',l)]
    print(f,len(e),e[:1],e[-1:])
    if e: print('  ',L[e[0]-1][:220])
    else: print(' first',L[0][:160])
