import json
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'] in('n1','n2','n3')]
keep.append({'id':'n4','role':'note','body':'Round4: board: Thread B opened DB_POOL_EXHAUSTED shipping-svc ongoing (round-04/board.md:3); Follow-up OPEN DATA_BACKFILL (round-04/board.md:4). changes: CHG-131 APPLIED TLS ticket rotation (round-04/changes.md:3). Logs: DNS SERVFAIL geo.internal continues inventory-svc (round-04/logs/inventory-svc.log:11,17,19,28,31,40,43,54,59,62,63,67,72) and ledger-svc (round-04/logs/ledger-svc.log:5,7,16,21,23,27,52). notify-worker disk usage /var/data 91-98% WARN (round-04/logs/notify-worker.log:2,6,17,20,26,38,55,61,69); shipping-svc disk 92-98% WARN (round-04/logs/shipping-svc.log:9,11,24,30,32,42,47) - NO db pool errors in shipping logs; suspect DISK_PRESSURE rather than DB pool. search-api still no errors.'})
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print('ok')