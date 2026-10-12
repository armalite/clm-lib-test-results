import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board.md empty. changes.md 3 lines (not yet read). WARN slow query lines are noise in all services. inventory-svc ERROR dns lookup failed host=rates.internal SERVFAIL at round-01/logs/inventory-svc.log:7,20,50,54,57,62,65 (DNS_RESOLUTION candidate).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read())
import glob
for p in glob.glob(b+'logs/*'):
  for i,l in enumerate(open(p),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and 'dns lookup' not in l: print(p.split('/')[-1],i,l.strip()[:140])