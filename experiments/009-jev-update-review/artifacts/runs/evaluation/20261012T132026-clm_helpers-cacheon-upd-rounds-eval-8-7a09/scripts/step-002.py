import os,json,re
b='/task/fixtures/round-01/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f).read().splitlines()):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l: print(f,i+1,l[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md: CHG-109 APPLIED TLS ticket rotation hourly; CHG-113 APPLIED notify-worker 8.20.0 sets db.pool_max=-4 (suspect BAD_CONFIG_ROLLOUT); CHG-114 APPLIED inventory-svc 8.20.0 no config. Logs r1: mostly slow query WARN noise.'}]}
json.dump(c,open('/task/workspace/context.json','w'))