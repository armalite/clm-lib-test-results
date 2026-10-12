import json
note='R1 findings: board.md empty. Slow query WARNs (200-450ms) on all services = background noise. inventory-svc: ERROR dns lookup failed host=rates.internal SERVFAIL at round-01/logs/inventory-svc.log:7,20,50,54,57,62,65,85,86,89,90 (DNS_RESOLUTION candidate). search-api output truncated; changes.md not yet read.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]}
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read()[:1500])
for i,l in enumerate(open(b+'logs/search-api.log'),1):
  if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l: print(i,l[:160])