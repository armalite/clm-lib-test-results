import os,json
b='/task/fixtures/round-07/'
for i,l in enumerate(open(b+'board.md'),1):print(i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
    L=open(b+'logs/'+f).read().splitlines()
    h=[(i,l) for i,l in enumerate(L,1) if ('ERROR' in l or 'error' in l.lower() or 'FATAL' in l) and 'slow query' not in l]
    print(f,len(h),[i for i,_ in h][:15])
    if h:print('  ',h[0][1][:220])
open('/task/workspace/notes.md','a').write('R7 read step19\n')