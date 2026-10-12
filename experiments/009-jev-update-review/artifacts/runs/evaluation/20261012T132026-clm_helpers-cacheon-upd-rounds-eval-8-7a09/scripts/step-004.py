import os,json
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines()): print(f,i+1,l[:200])
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f).read().splitlines()):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l: print(f,i+1,l[:160])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. round-01/changes.md: CHG-109 APPLIED TLS ticket rotation hourly; CHG-113 APPLIED notify-worker 8.20.0 sets db.pool_max=-4 (suspect BAD_CONFIG_ROLLOUT); CHG-114 APPLIED inventory-svc 8.20.0 no config. Logs r1: slow query WARN noise. R2 changes.md:3 CHG-114 PROPOSED raise HPA search tier (id reused; not applied).'}]}
json.dump(c,open('/task/workspace/context.json','w'))