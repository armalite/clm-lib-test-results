import re,ctx
ls=open('/task/fixtures/round-04/logs/auth-svc.log').read().splitlines()
from collections import Counter
c=Counter();first={}
for i,l in enumerate(ls):
    if re.search('WARN|ERROR',l) and 'slow query' not in l:
        k=re.sub(r'\d+','N',l[21:80]);c[k]+=1;first.setdefault(k,i+1)
for k in c: print(c[k],first[k],k)
n=ctx.load()['entries'][0]['body']
ctx.reset(n+'\nR4: board.md:3 Thread B MEMORY_LEAK auth-svc ongoing; board.md:4 VENDOR_TICKET OPEN. 429 tax-provider ERRORs in auth-svc.log (last :100) and shipping-svc.log:5-61 (UPSTREAM_RATE_LIMIT candidate). Pool WARNs inventory-svc.log:3-84, notify-worker.log:11-73. search-api clean.')