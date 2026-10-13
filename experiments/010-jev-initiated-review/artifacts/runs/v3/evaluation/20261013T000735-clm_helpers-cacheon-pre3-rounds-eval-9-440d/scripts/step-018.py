import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR4: board Thread B DB_POOL_EXHAUSTED shipping-svc ongoing (round-04/board.md:3); follow-up OPEN DATA_BACKFILL (round-04/board.md:4). changes: CHG-131 APPLIED TLS ticket rotation (round-04/changes.md:3). DNS SERVFAIL continues: round-04/logs/inventory-svc.log:11, ledger-svc.log:5,7. Disk usage high /var/data 91-98% on notify-worker (round-04/logs/notify-worker.log:2,6) and shipping-svc (round-04/logs/shipping-svc.log:9,11) -> DISK_PRESSURE candidate (board says DB pool; verify, no pool errors seen yet). search-api only slow queries. Next: advance to round 5."
c['entries']=[n]
json.dump(c,open(p,'w'))