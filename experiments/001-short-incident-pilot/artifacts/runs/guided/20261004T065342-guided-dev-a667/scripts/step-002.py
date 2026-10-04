import sys;sys.path.insert(0,'/task/workspace')
from helpers import ctx
ctx.compact('Notes: changes.log:14 CHG-4162 APPLIED shipping-api db.pool.max_size=12 (was 40) 08:28:20; :15 PROPOSED 56 not applied. config yaml:10 max_size 40 (superseded). oncall notes:5 stale. Hypothesis DB_POOL_EXHAUSTED.')
import re
for f in ['logs/shipping-api.log','logs/ingress-a.log']:
    n=0
    for i,l in enumerate(open('/task/fixtures/'+f),1):
        if re.search(r'pool|exhaust|ERROR|503',l,re.I):
            n+=1
            if n<=6: print(f,i,l.rstrip()[:160])
    print(f,'count',n)