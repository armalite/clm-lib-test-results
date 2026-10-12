import json,glob
b='/task/fixtures/round-01/'
for p in glob.glob(b+'logs/*'):
  for i,l in enumerate(open(p),1):
    if 'slow query' not in l and ('ERROR' in l or 'WARN' in l): print(p.split('/')[-1],i,l[:140].strip())
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: board empty. changes.md: CHG-113 APPLIED ledger-svc build 7.35.5 sets db.pool_max=0 (round-01/changes.md:3) -> likely BAD_CONFIG_ROLLOUT later. CHG-114 APPLIED checkout-api no config (line4). Logs r1: only background slow-query WARNs in all 5 svcs (noise).'}]}
json.dump(c,open('/task/workspace/context.json','w'))