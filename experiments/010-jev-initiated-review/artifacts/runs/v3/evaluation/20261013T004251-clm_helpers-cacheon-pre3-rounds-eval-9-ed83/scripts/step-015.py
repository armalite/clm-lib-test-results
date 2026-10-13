import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=c['entries'][0]['body']+"\nR4: board round-04/board.md:3 Thread B shipping-svc DB_POOL_EXHAUSTED ongoing (no pool errors in shipping logs R4; only disk WARNs); :4 follow-up OPEN DATA_BACKFILL. round-04/changes.md:3 CHG-131 APPLIED TLS ticket rotation. DNS SERVFAIL continues inventory round-04/logs/inventory-svc.log:11-72, ledger round-04/logs/ledger-svc.log:5-52. disk usage high /var/data 91-98% notify-worker round-04/logs/notify-worker.log:2-69 and shipping-svc round-04/logs/shipping-svc.log:9-47 (DISK_PRESSURE candidate). Add 'inflight' to grep."
c['entries']=[{'id':'n1','role':'note','body':n}]
json.dump(c,open(p,'w'))
print('ok')