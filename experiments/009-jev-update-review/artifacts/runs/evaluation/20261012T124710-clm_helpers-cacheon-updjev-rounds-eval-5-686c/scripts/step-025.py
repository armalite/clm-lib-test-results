import json,re
from collections import Counter
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
  c=Counter();first={}
  for i,l in enumerate(open(f'/task/fixtures/round-09/logs/{s}.log'),1):
    if re.search('(?i)error|pool|disk|cert|tls|429|memory|lag|dns',l) and 'slow query' not in l.lower():
      m=re.search(r'"msg":"([^"]+)',l);k=m.group(1) if m else l[:60]
      c[k]+=1;first.setdefault(k,[]).append(i)
  for k,v in c.items():print(s,v,k[:70],first[k][:6])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace('NEXT: advance to R9.','R8 auth tls failed continues (round-08/logs/auth-svc.log:6,9,29,32). R9: no board/changes.')
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))