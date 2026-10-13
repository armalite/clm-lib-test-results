import json
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: CHG-107 APPLIED retry budget idempotent GETs=1 (round-01/changes.md:3). board empty. Logs: all services have background slow query WARNs (noise). inventory-svc DNS SERVFAIL host=rates.internal at round-01/logs/inventory-svc.log:7,20,50,54,57,62,65,85-90 (DNS_RESOLUTION candidate). search-api output truncated after line 31; check search/shipping ERRORs excluding slow query next.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import glob,re
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if 'slow query' not in l and re.search(r'ERROR|WARN',l) and 'inventory' not in p:print(p.split('/')[-1],i,l.strip()[:140])