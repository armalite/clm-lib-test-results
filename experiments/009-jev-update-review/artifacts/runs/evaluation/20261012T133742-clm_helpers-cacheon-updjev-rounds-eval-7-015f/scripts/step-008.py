import json,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if ('ERROR' in l or '429' in l or 'pool' in l) and 'slow query' not in l:
            print(f.split('/')[-1],i,l.strip()[:110])
b='R1: CHG-113 APPLIED ledger-svc pool_max=0 r1 changes.md:3 (suspect BAD_CONFIG, no ledger errors r1-r2). R2: board.md:3 OPEN POSTMORTEM_DRAFT; shipping 429 tax-provider round-02/logs/shipping-svc.log:7,22,35. R3: board.md:3 Thread A UPSTREAM_RATE_LIMIT shipping-svc+search-api ongoing; board.md:4 OPEN DATA_BACKFILL; :5 OPEN CAPACITY_REVIEW; changes.md:3 CHG-124 TLS ticket rotation (watch CERT).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))