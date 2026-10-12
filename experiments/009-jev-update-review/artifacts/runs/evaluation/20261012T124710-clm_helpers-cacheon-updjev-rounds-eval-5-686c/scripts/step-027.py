import json,re
from collections import Counter
for s in ['checkout-api','auth-svc','search-api','shipping-svc','ledger-svc']:
  c=Counter();f={}
  for i,l in enumerate(open(f'/task/fixtures/round-10/logs/{s}.log'),1):
    if re.search('(?i)error|pool|disk|cert|tls|429|memory|lag|dns|fail|warn',l) and 'slow query' not in l.lower():
      m=re.search(r'"msg":"([^"]+)',l);k=m.group(1) if m else l[:80]
      c[k]+=1;f.setdefault(k,[]).append(i)
  for k,v in c.items():print(s,v,k[:80],f[k][:6])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body']+'\nR10: Thread C opened checkout-api request failures cause unknown, ongoing (round-10/board.md:3). CHG-173 PROPOSED ignore.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))