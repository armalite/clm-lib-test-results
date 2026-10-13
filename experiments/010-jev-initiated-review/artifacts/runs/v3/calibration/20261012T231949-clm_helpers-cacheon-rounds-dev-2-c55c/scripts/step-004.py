import json,glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for p in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(p)):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l:print(p.split('/')[-1],i+1,l.strip()[:130])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. slow query WARNs noise. inventory-svc DNS SERVFAIL host=rates.internal round-01/logs/inventory-svc.log:7,20,50,54,57,62,65. round-01/changes.md: CHG-107 APPLIED retry budget idempotent GETs=1. R2 released; see s4 obs.'}]}
json.dump(c,open('/task/workspace/context.json','w'))