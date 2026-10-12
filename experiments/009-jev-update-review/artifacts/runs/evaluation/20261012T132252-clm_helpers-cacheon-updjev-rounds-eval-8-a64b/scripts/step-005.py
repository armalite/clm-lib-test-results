import json,glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|CRIT',l):print(f.split('/')[-1],i,l.rstrip()[:160])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md: CHG-109 APPLIED TLS ticket rotation hourly (round-01/changes.md:3); CHG-113 APPLIED notify-worker 8.20.0 sets db.pool_max=-4 (round-01/changes.md:4) -> suspect BAD_CONFIG_ROLLOUT; CHG-114 APPLIED inventory-svc 8.20.0 no config (round-01/changes.md:5). NOTE R2 changes.md:3 reuses id CHG-114 as PROPOSED HPA search tier (different change, not applied; irrelevant). Logs R1: only slow query WARNs (noise).'}]}
json.dump(c,open('/task/workspace/context.json','w'))