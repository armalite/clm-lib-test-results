import json
n1='R1: board empty. r01 changes.md:3 CHG-112 APPLIED retry budget GETs=1. Services: notify-worker, shipping-svc, checkout-api, ledger-svc, inventory-svc. Log fmt: ts LEVEL svc msg k=v. Slow query ~230-450ms is noise; request ok/gc/health/heartbeat noise.'
n2='R2: board empty. changes.md:4 CHG-120 APPLIED 5.26.1 shipping-svc db.pool_max=-4 (SUSPECT BAD_CONFIG_ROLLOUT, no shipping errors yet r02); changes.md:3 CHG-118 TLS ticket rotation; :5 CHG-121 inventory no config. r02 notify-worker.log pool exhausted lines 6-60.'
n3='R3: board.md:3 Thread A DB_POOL_EXHAUSTED notify-worker + ledger-svc, ongoing. board.md:4 Thread B inventory-svc suspected DISK_PRESSURE ongoing, BUT logs show heap usage high (rss 2153-3670) lines 4,7,20,24,31,46,63 -> likely MEMORY_LEAK. changes.md:3 CHG-122 retry budget. r03 ledger pool exhausted lines 1-71; notify lines 5-72. shipping/checkout quiet r03.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2},{'id':'n3','role':'note','body':n3}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')