import json
n={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'Round1 facts: changes.md:3 CHG-107 APPLIED retry budget idempotent GETs=1. board.md empty. Logs: slow query WARNs on all services (likely noise). inventory-svc DNS SERVFAIL host=rates.internal at round-01/logs/inventory-svc.log:7,20,50,54,57,62,65,85,86,89,90 (increasing) -> candidate DNS_RESOLUTION inventory-svc. search-api/shipping-svc output truncated; check shipping-svc and search-api non-slow-query errors next round. Context edits need begin_review first.'}]}
json.dump(n,open('/task/workspace/context.json','w'))
import re
for s in ['shipping-svc','search-api']:
  for i,l in enumerate(open(f'/task/fixtures/round-01/logs/{s}.log'),1):
    if re.search(r'ERROR|WARN',l) and 'slow query' not in l:print(s,i,l.strip()[:120])