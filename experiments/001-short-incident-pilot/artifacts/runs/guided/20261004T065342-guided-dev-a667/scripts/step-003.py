import sys;sys.path.insert(0,'/task/workspace')
from helpers import ctx
ctx.compact('Notes: changes.log:14 CHG-4162 APPLIED shipping-api db.pool.max_size=12 (was 40) 08:28:20; :15 PROPOSED 56 not applied. config yaml:10 max_size 40 (superseded). oncall notes:5 stale. ingress-a.log:272-287 503 upstream timeout from 08:31. Hypothesis DB_POOL_EXHAUSTED.')
import re
n=0
for i,l in enumerate(open('/task/fixtures/logs/shipping-api.log'),1):
    if re.search(r'WARN|ERROR',l) and re.search(r'pool|connection',l,re.I):
        n+=1
        if n<=4: print(i,l.rstrip()[:200])
print('count',n)
for i,l in enumerate(open('/task/fixtures/metrics/shipping-api.csv'),1):
    if i==1 or i in (60,70,80): print(i,l.rstrip())