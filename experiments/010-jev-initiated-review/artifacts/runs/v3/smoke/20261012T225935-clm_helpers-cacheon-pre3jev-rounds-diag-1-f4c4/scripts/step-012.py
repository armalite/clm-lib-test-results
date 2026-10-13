import json
n1='Round1: board empty. r01 changes.md:3 CHG-112 APPLIED retry budget idempotent GETs=1. Services: notify-worker, shipping-svc, checkout-api, ledger-svc, inventory-svc. Log fmt: ts LEVEL svc msg k=v. Slow query baseline ~230-450ms (normal noise).'
n2='Round2: board empty. changes.md:3 CHG-118 APPLIED TLS ticket rotation hourly; changes.md:4 CHG-120 APPLIED build 5.26.1 shipping-svc sets db.pool_max=-4 (SUSPECT BAD_CONFIG_ROLLOUT); changes.md:5 CHG-121 APPLIED 5.26.1 inventory-svc no config. R2 checkout/inventory/ledger: baseline only. r02 notify-worker.log: db pool exhausted WARNs lines 6,12,14,23,30,34,36,53,57,59,60 (in_use 16/16,20/20,10/10) -> DB_POOL_EXHAUSTED candidate notify-worker. shipping r02 non-slow lines in spill/s10.obs.txt.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))
import collections
t=open('/task/workspace/spill/s10.obs.txt').read().splitlines()
cnt=collections.Counter()
for l in t:
  p=l.split(None,4)
  if len(p)>4:
    m=' '.join(w for w in p[4].split() if '=' not in w)
    cnt[m]+=1
    if cnt[m]<=2:print(l[:120])
print(cnt.most_common(8))