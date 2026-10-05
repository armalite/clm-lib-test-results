import json
n1='R1: board empty. slow query WARNs = noise. inventory-svc db pool exhausted WARN round-01/logs/inventory-svc.log:5,9,28,30,45,52. changes r01: CHG-113 APPLIED search-api 8.23.7 sets cache.ttl_s=-1 (round-01/changes.md:4, suspect BAD_CONFIG_ROLLOUT); CHG-114 auth-svc no config; CHG-107 PROPOSED only.'
n2='R2: board.md:3 Thread A opened DB_POOL_EXHAUSTED inventory-svc + notify-worker, ongoing. pool WARNs round-02/logs/inventory-svc.log:3-19, notify-worker.log:6-45. no other errors r2 (search-api quiet). Next: advance.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')