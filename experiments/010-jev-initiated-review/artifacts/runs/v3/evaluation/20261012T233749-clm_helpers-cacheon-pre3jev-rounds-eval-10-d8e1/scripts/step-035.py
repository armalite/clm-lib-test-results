import re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read())
for s in ['shipping-svc','search-api','inventory-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search('ERROR|429|config',l)]
    print(s,len(h),h[:3],h[-3:])
    if h: print(L[h[0]-1][:200])