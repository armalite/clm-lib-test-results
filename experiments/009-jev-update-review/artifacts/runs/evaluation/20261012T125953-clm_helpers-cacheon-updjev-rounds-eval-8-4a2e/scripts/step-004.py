import json,glob
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. r1 changes.md:3 CHG-109 APPLIED TLS ticket rotation hourly; r1 changes.md:4 CHG-113 APPLIED notify-worker build 8.20.0 sets db.pool_max=-4 (suspect BAD_CONFIG_ROLLOUT); r1 changes.md:5 CHG-114 inventory-svc 8.20.0 no config. Logs r1: only slow query WARNs (noise). R2 changes.md:3 CHG-114 PROPOSED HPA search tier (not applied; id reused, irrelevant).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-02/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'slow query' not in l and 'INFO' not in l:print(f.split('/')[-1],i,l[:140].rstrip())