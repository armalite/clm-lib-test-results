import json
n1='Round1: board empty. r01 changes.md:3 CHG-112 APPLIED retry budget idempotent GETs=1. Services: notify-worker, shipping-svc, checkout-api, ledger-svc, inventory-svc. Log fmt: ts LEVEL svc msg k=v. Slow query baseline ~230-450ms (normal noise).'
n2='Round2: board empty. changes.md:3 CHG-118 APPLIED TLS ticket rotation hourly; changes.md:4 CHG-120 APPLIED build 5.26.1 shipping-svc sets db.pool_max=-4 (SUSPECT BAD_CONFIG_ROLLOUT); changes.md:5 CHG-121 APPLIED 5.26.1 inventory-svc no config. R2 logs checked checkout/inventory/ledger: only baseline slow queries. Still to check r02 notify-worker & shipping-svc logs (spill/s5.obs.txt lines after 30).'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s5.obs.txt').read().splitlines()
for l in t:
  if l.startswith(('notify','shipping')) and 'slow query' not in l:print(l[:140])