import json,glob
b='/task/fixtures/round-02/'
for p in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(p),1):
    if 'slow query' not in l and ('ERROR' in l or 'WARN' in l or 'error' in l): print(p.split('/')[-1],i,l[:150].strip())
print(open(b+'board.md').read())
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: board empty. CHG-113 APPLIED ledger-svc build 7.35.5 sets db.pool_max=0 (round-01/changes.md:3) -> likely BAD_CONFIG_ROLLOUT later. CHG-114 APPLIED checkout-api no config (r1 changes.md:4). R1 logs: only slow-query WARN noise. R2: board.md:3 follow-up OPEN POSTMORTEM_DRAFT; CHG-119 APPLIED dashboards (noise).'}]}
json.dump(c,open('/task/workspace/context.json','w'))