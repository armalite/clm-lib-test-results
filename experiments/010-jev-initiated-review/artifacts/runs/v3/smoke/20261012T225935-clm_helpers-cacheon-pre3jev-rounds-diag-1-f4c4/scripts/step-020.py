import json
n1='R1: board empty. r01 changes.md:3 CHG-112 APPLIED retry budget GETs=1. Services: notify-worker, shipping-svc, checkout-api, ledger-svc, inventory-svc. Log fmt: ts LEVEL svc msg k=v. Noise: slow query, request ok/gc/health/heartbeat.'
n2='R2: board empty. changes.md:4 CHG-120 APPLIED 5.26.1 shipping-svc db.pool_max=-4 (SUSPECT BAD_CONFIG_ROLLOUT, no shipping errors yet); changes.md:3 CHG-118 TLS ticket rotation; :5 CHG-121 inventory no config. r02 notify-worker.log pool exhausted lines 6-60.'
n3='R3: board.md:3 Thread A DB_POOL_EXHAUSTED notify-worker + ledger-svc, ongoing. board.md:4 Thread B inventory-svc suspected DISK_PRESSURE ongoing, BUT logs show heap high lines 4,7,20,24,31,46,63 -> likely MEMORY_LEAK. r03 ledger pool exhausted 1-71; notify 5-72.'
n4='R4: board.md:3 follow-up OPEN VENDOR_TICKET; board.md:4 OPEN DATA_BACKFILL. changes.md:3 CHG-129 log sampling (noise). ledger pool exhausted lines 6-72; notify 2-62. inventory/shipping/checkout quiet r04 (inventory heap gone?).'
c={'format':'clm-context/v1','entries':[{'id':i,'role':'note','body':b} for i,b in [('n1',n1),('n2',n2),('n3',n3),('n4',n4)]]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')