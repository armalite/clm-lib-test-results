import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board.md:3 Thread B ledger-svc QUEUE_BACKLOG ongoing (suspected). changes.md:3 CHG-129 PROPOSED only. ledger-svc.log 429s lines 2-37 (7x) -> maybe UPSTREAM_RATE_LIMIT not queue; ERR line 53. inventory-svc cert_expired lines 3-62. checkout-api many WARNs (unclassified). Next: inspect ledger/checkout round4 then advance to round 5.'})
json.dump(c,open('/task/workspace/context.json','w'))
import re
for f in ['ledger-svc','checkout-api']:
  L=open('/task/fixtures/round-04/logs/%s.log'%f).read().splitlines()
  for i in [1,9,52]:
    if i<len(L):print(f,i+1,L[i][:160])