import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|pool|cert|DNS|OOM|disk|cache',l,re.I) and n<3:
      print(f.split('/')[-1],i,l.strip()[:140]);n+=1
nb='R1: CHG-113 APPLIED ledger-svc 7.35.5 db.pool_max=0 (round-01/changes.md:3) -> likely BAD_CONFIG_ROLLOUT later. R2: OPEN POSTMORTEM_DRAFT (round-02/board.md:3). R3: Thread A UPSTREAM_RATE_LIMIT tax-provider 429 shipping-svc+search-api ongoing (round-03/board.md:3; logs round-03/logs/search-api.log:2, shipping-svc.log:5); OPEN DATA_BACKFILL (r3 board.md:4), CAPACITY_REVIEW (r3 board.md:5); CHG-124 TLS noise. R4: Thread B checkout-api CACHE_STAMPEDE ongoing (round-04/board.md:3); CHG-128 log sampling noise.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':nb}]},open('/task/workspace/context.json','w'))