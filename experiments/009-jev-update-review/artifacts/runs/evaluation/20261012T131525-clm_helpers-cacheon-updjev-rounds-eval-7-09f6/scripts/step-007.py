import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'429|pool|ERROR|error|exhaust',l): print(f.split('/')[-1],i,l.strip()[:110])
n='R1: CHG-113 APPLIED round-01/changes.md:3 ledger-svc build 7.35.5 sets db.pool_max=0 (suspect BAD_CONFIG_ROLLOUT). CHG-114 checkout-api no config (r1 changes.md:4). Svcs: checkout-api, ledger-svc, payments-svc, search-api, shipping-svc. R2: board.md:3 followup OPEN POSTMORTEM_DRAFT. R2 shipping 429 round-02/logs/shipping-svc.log:7,22,35-41,60. R3: board.md:3 Thread A UPSTREAM_RATE_LIMIT shipping-svc+search-api ongoing; board.md:4 OPEN DATA_BACKFILL; board.md:5 OPEN CAPACITY_REVIEW; CHG-124 TLS ticket rotation (r3 changes.md:3, likely irrelevant).'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))