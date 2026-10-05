import json,re
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: CHG-107 APPLIED retry budget GETs=1 (round-01/changes.md:3). slow query WARNs = noise. inventory-svc DNS SERVFAIL host=rates.internal round-01/logs/inventory-svc.log:7,20.\nR2: board Thread A DNS_RESOLUTION inventory-svc+checkout-api ongoing (round-02/board.md:3). CHG-120 APPLIED search-api http.max_inflight=-1 (round-02/changes.md:3) watch BAD_CONFIG. CHG-121 auth no config. checkout DNS errs round-02/logs/checkout-api.log:8,24; inventory round-02/logs/inventory-svc.log:8,12.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-02/logs/search-api.log'),1):
  if 'slow query' not in l and not re.search(r' INFO ',l): print(i,l.strip()[:150])