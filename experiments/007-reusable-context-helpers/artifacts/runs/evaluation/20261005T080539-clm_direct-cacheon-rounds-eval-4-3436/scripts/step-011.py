import re
b='/task/fixtures/round-04/'
print(open(b+'board.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
    L=open(b+'logs/'+f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search('WARN|ERROR|FATAL',l) and 'slow query' not in l]
    print(f,len(hits))
    for i,l in hits[:4]: print(' ',i,l[:150])