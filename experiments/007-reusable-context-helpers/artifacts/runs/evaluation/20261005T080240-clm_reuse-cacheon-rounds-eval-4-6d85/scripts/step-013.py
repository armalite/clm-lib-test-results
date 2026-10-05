import re,glob
from collections import Counter
for f in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-05/'+f).read().splitlines()):print(f,i+1,l)
for p in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    ls=open(p).read().splitlines();c=Counter();fl={}
    for i,l in enumerate(ls):
        if re.search('WARN|ERROR|warn|error',l) and 'slow query' not in l:
            k=re.sub(r'\d+','N',l[19:85]);c[k]+=1;fl.setdefault(k,[i+1,i+1]);fl[k][1]=i+1
    print(p.split('/')[-1],len(ls))
    for k in c:print(' ',c[k],fl[k],k)