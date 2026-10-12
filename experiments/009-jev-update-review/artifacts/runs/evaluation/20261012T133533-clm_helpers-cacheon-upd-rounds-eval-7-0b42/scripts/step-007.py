import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|429|pool|cert|DNS|OOM|disk',l,re.I) and n<4:
      print(f.split('/')[-1],i,l.strip()[:150]);n+=1
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: CHG-113 APPLIED ledger-svc 7.35.5 db.pool_max=0 (round-01/changes.md:3) -> likely BAD_CONFIG_ROLLOUT later. R2: OPEN POSTMORTEM_DRAFT (round-02/board.md:3); shipping-svc 429 tax-provider (round-02/logs/shipping-svc.log:7,22). R3: Thread A UPSTREAM_RATE_LIMIT shipping-svc+search-api ongoing (round-03/board.md:3); OPEN DATA_BACKFILL (board.md:4), CAPACITY_REVIEW (board.md:5); CHG-124 TLS ticket rotation (r3 changes.md:3, noise?).'}]}
json.dump(c,open('/task/workspace/context.json','w'))